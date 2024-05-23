import unittest
from task_extractor.extractor import TaskExtractor


class checkAdd(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.task_extractor = TaskExtractor()
        super().__init__(methodName)
    def check(self, text, name, task_type, time, periodicity, is_done, is_cancelled):
        self.task_extractor.run(text)
        self.assertEqual(self.task_extractor.tasks[0].name, name, "TASK NAME DIDN'T MATCH!")
        self.assertEqual(self.task_extractor.tasks[0].task_type, task_type, "TASK TYPE DIDN'T MATCH")
        self.assertEqual(self.task_extractor.tasks[0].time, time, "TIMES DIDN'T MATCH")
        self.assertEqual(self.task_extractor.tasks[0].periodicity, periodicity, "PERIODICITIES DIDN'T MATCH")
        self.assertEqual(self.task_extractor.tasks[0].is_done, is_done,"IS_DONE WRONG!")
        self.assertEqual(self.task_extractor.tasks[0].is_cancelled, is_cancelled, "IS_CANCELLED WRONG!")
    ##########################################
    ############### testcases ################
    ############# 1 ############################
    def test_1(self):
        text = "یادم باشد تسک مدرسه را فردا انجام دهم."
        name = "مدرسه"
        task_type = "add"
        time = "فردا"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ############# 2 ##################
    def test_2(self):
        text = "باید هر ۳ روز یکبار مشق‌هایم را بنویسم"
        name = "مشق‌هایم"
        task_type = "add"
        time = ""
        periodicity = "هر ۳ روز یکبار"
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ################ 3 ###################
    def test_3(self):
        text = "نیاز به یادآوری دارم تا ۵ اردیبهشت قرصم را بخورم."
        name = "قرصم"
        task_type = "add"
        time = "۵ اردیبهشت"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ############ 4 ##################
    def test_4(self):
        text = "یادم باشد هر روز ساعت ۸ صبح به جلسه اسکرام بروم."
        name = "جلسه اسکرام"
        task_type = "add"
        time = "۸ صبح"
        periodicity = "هرروز"
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ############ 5 ############
    def test_5(self):
        text = "یادم باشد مسابقه تنیس امشب را حتما با بروبچ ببینم."
        name =  "مسابقه تنیس"
        task_type = "add"
        time = "امشب"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ############ 6 ###############
    def test_6(self):
        text = "حتما کار خیریه موسسه اکبر را در تاریخ ۳۰ فروردین پیگیری بکنم."
        name =  "خیریه موسسه اکبر"
        task_type = "add"
        time = "۳۰ فروردین"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ######### 7 ################
    def test_7(self):
        text = "یادم باشه تسک شستن ماشین آقا رضا رو فردا ۵ صبح انجام بدم."
        name =  "شستن ماشین آقا رضا"
        task_type = "add"
        time = "فردا ۵ صبح"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ######## 8 #################
    def test_8(self):
        text = "یادم باشه وظیفه شستن ماشین را آخر هفته تموم کنم."
        name =  "شستن ماشین"
        task_type = "add"
        time = ""
        periodicity = "آخر هفته"
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ######## 9 ############
    def test_9(self):
        text = "یادم باشه وظیفه شستن ماشین رو آخر هفته تموم کنم."
        name =  "شستن ماشین"
        task_type = "add"
        time = ""
        periodicity = "آخر هفته"
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ########## 10 ###########
    def test_10(self):
        text = "جلسه اتوکشی را به تقویمم برای روز ۲۱ فروردین اضافه کن."
        name =  "اتوکشی"
        task_type = "add"
        time = "۲۱ فروردین"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    ######### 11 ##########
    def test_11(self):
        text = "وظیفه شستن ظروف آقای امیری را برای روز ۳۰ دی ساعت ۴:۳۰ یادآوری کن."
        name =  "شستن ظروف آقای امیری"
        task_type = "add"
        time = "۳۰ دی ساعت ۴:۳۰"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
if __name__=="__main__":
    unittest.main()