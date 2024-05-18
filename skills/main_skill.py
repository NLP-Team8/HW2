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
        if message.text == 'بگو':
            # print('--------------------------------------')
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            res = cur.execute("SELECT * FROM tasks")
            ans = res.fetchall()
            await message.respond(str(ans))
            return

        # await message.respond('Hey, I love Alireza Amiri!')

        print("Pending")
        extractor = TaskExtractor()
        extractor.run(message.text)

        for task in extractor.tasks:
            self.add_to_db(task)

        await message.respond(str(extractor.tasks))
    
    def add_to_db(self, task):
        username, name, time, period, done, cancel = 'ali12', task.name, task.start_date, task.end_date, int(task.is_done), int(task.is_cancelled)
        self.cur.execute(f" INSERT INTO tasks VALUES ('{username}', '{name}', '{time}', '{period}', {done}, {cancel})")
        self.con.commit()
    def cancel_task(self, task):
        self.cur.execute(f"UPDATE tasks SET is_cancelled=1 WHERE name={task.name} AND user={task.username}")
        self.con.commit()
    

  