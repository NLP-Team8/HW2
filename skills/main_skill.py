from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from task_extractor.extractor import TaskExtractor
import sqlite3

class HelloSkill(Skill):
    def __init__(self, opsdroid, config):
        super(HelloSkill, self).__init__(opsdroid, config)
        self.db_file = config.get("database", "opsdroid.db")
        self.con = sqlite3.connect(self.db_file)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks(user, name, time, period, done, cancel)")


    @match_regex(r'.*')
    async def hello(self, message):
        if message.text.strip() == 'بگو':
            # print('--------------------------------------')
            res = self.cur.execute(f"SELECT * FROM tasks WHERE user='{message.user}'")
            ans = res.fetchall()
            await message.respond(str(ans))
            return
        if message.text.strip() == 'ریست':
            self.cur.execute(f"DELETE FROM tasks")
            self.con.commit()
            await message.respond('همه تسک‌ها پاک شد.')
            return
        if message.text.strip() == 'راهنما':
            response_text = '''
با استفاده از پیامی مانند "یادم باشه کتاب را ساعت 8:0 روز 5 تیر بخوانم. می‌توانید تسک‌ اضافه کنید.
با پیامی مانند تسک کتاب را کنسل بکن می‌توانید تسک را کنسل کنید.
با پیامی مانند تسک کتاب تمام شد نیز می‌توانید اتمام تسک را به برنامه اضافه کنید.
می‌توانید زمان یک تسک را نیز با گفتن دوباره آن با زمان جدید عوض کنید.
با پیام ریست کل تسک‌ها از دیتابیس پاک می‌شوند.
'''
            await message.respond(response_text)
            return
        


        # await message.respond('Hey, I love Alireza Amiri!')

        print("Pending Response to", message.user)
        extractor = TaskExtractor()
        extractor.run(message.text)

        for task in extractor.tasks:
            if task.task_type == "cancelation":
                self.cancel_task(task, message.user)
            if task.task_type == "done":
                self.finish_task(task, message.user)
            if task.task_type == "change":
                self.change_task_time(task, message.user)
            if task.task_type == "add":
                self.add_task(task, message.user)

        await message.respond(str(extractor.tasks))
    
    def add_task(self, task, username):
        username, name, time, period, done, cancel = username, task.name, task.time, task.periodicity, int(task.is_done), int(task.is_cancelled)
        self.cur.execute(f" INSERT INTO tasks VALUES ('{username}', '{name}', '{time}', '{period}', {done}, {cancel})")
        self.con.commit()
    
    def cancel_task(self, task, username):
        self.cur.execute(f"UPDATE tasks SET cancel=1 WHERE name='{task.name}' AND user='{username}'")
        self.con.commit()
    
    def change_task_time(self, task, username):
        self.cur.execute(f"UPDATE tasks SET time='{task.time}' WHERE name='{task.name}' AND user='{username}'")
        self.con.commit()
    
    def finish_task(self, task, username):
        self.cur.execute(f"UPDATE tasks SET done=1 WHERE name='{task.name}' AND user='{username}'")
        self.con.commit()
    

  