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
        time =  "ساعت ۸ صبح"
        periodicity = "هر روز"
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

class check_cancell(unittest.TestCase):
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
    
    def test_1(self):
        text = "جلسه اسکرام روزانه ام را لغو کن."
        name =  "اسکرام"
        task_type = "cancelation"
        time = ""
        periodicity = "روزانه"
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_2(self):
        text = "جلسه اسکرام را لغو کن."
        name =  "اسکرام"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_3(self):
        text = "کار طی زدن زمین به حول و قوه الهی کنسل شد."
        name =  "طی زدن زمین"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_4(self):
        text = "تسک طی زدن زمین کنسل شد."
        name =  "طی زدن زمین"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_5(self):
        text = "امشب جلسه سران قوا بود که کنسل شد."
        name =  "سران قوا"
        task_type = "cancelation"
        time = "امشب"
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_6(self):
        text = "وظیفه شستن ماشین آقای امیری عشق کنسل شد."
        name =  "شستن ماشین آقای امیری عشق"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_7(self):
        text = "کار بیگاری را کنسل بکن."
        name =  "بیگاری"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_8(self):
        text = "کار بیگاری را کنسل نکن."
        name =  "بیگاری"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_9(self):
        text = "آقای امیری جلسه اسکرام را لغو کرد."
        name =  "اسکرام"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_10(self):
        text = "آقای امیری جلسه اسکرام را لغو کردند."
        name =  "اسکرام"
        task_type = "cancelation"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_11(self):
        text = "یادآوری کن که آقای امیری جلسه جوجه خوری در ساعت ۵:۳۰ روز ۳۰ فروردین را لغو کردند."
        name =  "جوجه خوری"
        task_type = "cancelation"
        time = "ساعت ۵:۳۰ ۳۰ فروردین"
        periodicity = ""
        is_done = False
        is_cancelled = True
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass

class check_done(unittest.TestCase):
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
    def test_1(self):
        text = "کار ساختن بات انجام شد."
        name =  "ساختن بات"
        task_type = "done"
        time = ""
        periodicity = ""
        is_done = True
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_2(self):
        text = "من و اقا رضا پنجنشبه تسک خوردن بستنی را تمام کردیم."
        name =  "خوردن بستنی"
        task_type = "done"
        time = "پنجشنبه"
        periodicity = ""
        is_done = True
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_3(self):
        text = "جلسه ختم مرحوم مغفور با موفقیت تمام شد."
        name =  "ختم مرحوم مغفور"
        task_type = "done"
        time = ""
        periodicity = ""
        is_done = True
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_4(self):
        text = "آخر هفته من و آقای امیری به استادیوم رفتیم و وظیفه نظارت بر بازی را انجام دادیم."
        name =  "نظارت بر بازی"
        task_type = "done"
        time = "آخر هفته"
        periodicity = ""
        is_done = True
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_5(self):
        text = "کار ساختن بات متاسفانه تمام نشد."
        name =  "ساختن بات"
        task_type = "done"
        time = ""
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass

class check_change(unittest.TestCase):
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
    def test_1(self):
        text = "زمان جلسه اسکرام را به ساعت ۵:۲۴ تغییر بده"
        name =  "اسکرام"
        task_type = "change"
        time = "ساعت ۵:۲۴"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_2(self):
        text = "کار بانجی جامپینگ را به روز ۲۴ اردیبهشت به تعویق بینداز."
        name =  "بانجی جامپینگ"
        task_type = "change"
        time = "۲۴ اردیبهشت"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_3(self):
        text = "ساعت تسک یوگا را به ۱۲ ظهر شنبه تغییر بده."
        name =  "یوگا"
        task_type = "change"
        time = "۱۲ ظهر شنبه"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_4(self):
        text = "برنامه عبدالمجید رااز روز ۲۳ فروردین به روز ۲۵ خرداد ساعت ۳:۰۱ به تاخیر بینداز"
        name =  "برنامه عبدالمجید"
        task_type = "change"
        time = "۲۵ خرداد ساعت ۳:۰۱"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_5(self):
        text = "زمان بازی هاکی را به ساعت ۶ عصر تغییر بده."
        name =  "بازی هاکی"
        task_type = "change"
        time = "ساعت ۶ عصر"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
    def test_6(self):
        text = "کار بانجی جامپینگ را به روز ۲۴ اردیبهشت تغییر بده."
        name =  "بانجی جامپینگ"
        task_type = "change"
        time = "۲۴ اردیبهشت"
        periodicity = ""
        is_done = False
        is_cancelled = False
        self.check(text, name, task_type, time, periodicity, is_done, is_cancelled)
        pass
if __name__=="__main__":
    unittest.main()