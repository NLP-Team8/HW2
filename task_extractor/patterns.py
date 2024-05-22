from task_extractor.parser import MixedRegexpParser

class Patterns:
        ANY = r"[^']+"
        ANY_P = r"'[^']+'"
        ANY_T = f"(?:<{ANY_P},{ANY_P}>)"
        AGG_WORDS = lambda tag, words: f"(?:<'(?:{'|'.join(words)})','{tag}'>)"
        AGG_P = lambda patterns: f"(?:{'|'.join(patterns)})"
        NOUN = f"(?:<{ANY_P},'NOUN'>)"
        ADJ = f"(?:<{ANY_P},'ADJ'>)"
        NUM = f"(?:<{ANY_P},'NUM'>)"
        VERB = f"(?:<{ANY_P},'VERB'>)"
        ADP = f"(?:<{ANY_P},'ADP'>)"
        SCONJ = f"(?:<{ANY_P},'SCONJ'>)"
        ADV = f"(?:<{ANY_P},'ADV'>)"
        CCONJ = f"(?:<{ANY_P},'CCONJ'>)"
        DET = f"(?:<{ANY_P},'DET'>)"

        
        NUM_GROUP = f"(?:{NUM}(?:{CCONJ}{NUM})*)"
        NP = f"(?:{DET}?{ADJ}?{NOUN}(?:{NOUN}|{ADJ}|{NUM_GROUP})*)"
        NP_GROUP = f"(?:{NP}(?:{CCONJ}{NP})*)"
        VP = f"(?:(?:{NOUN}|{ADJ})?{VERB})"
        MONTH = f"(?:{AGG_WORDS('NOUN', ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'])})"
        ADJECTIVES =f"(?:{AGG_WORDS('NOUN', ['زوج', 'فرد'])})"
        TIME1 = r"(?:<'\d+:\d+(?::\d+)?','NUM'>)"
        TIME2 = r"(?:<'\d+','NUM'>)"
        TIME = f"(?:{TIME1}|{TIME2})"
        SAAT_WORD = f"(?:{AGG_WORDS('NOUN', [ 'ساعت'])})"
        DAY_NIGHT = f"(?:{AGG_WORDS('NOUN', [ 'صبح', 'شب', 'عصر', 'ظهر', 'روز'])})"
        DAYS = f"(?:{AGG_WORDS('NOUN', ['شنبه', 'یکشنبه', 'دوشنبه', 'سهشنبه', 'چهارشنبه', 'پنچشنبه', 'جمعه'])})" 
        DAYS2 = f"(?:{AGG_WORDS('ADV', ['فردا', 'امروز', 'امشب', ])}|{AGG_WORDS('NOUN', ['فردا', 'امروز', 'امشب', ])})"
        DATE = f"(?:{NUM_GROUP}{MONTH}|{DAYS}|{DAYS2})"
        DATETIME = f"(?:{DATE}{TIME}|{TIME}{DATE}|{DATE}|{TIME})"
        SAAT_REGEX = f"(?:{SAAT_WORD}{TIME}{DAY_NIGHT}?{DATE}|{DATE}{SAAT_WORD}?{TIME}{DAY_NIGHT}|{DATE}{SAAT_WORD}{TIME}{DAY_NIGHT}?|{SAAT_WORD}{TIME}{DAY_NIGHT}?|{TIME}{DAY_NIGHT}|{DATE}|{TIME})"
        TASK_WORDS = ['وظیفه', 'تسک', 'کار', 'جلسه']
        # PERIODICITY_WORDS= ['هر روز', 'دو روز یک بار', 'سه روز یکبار', 'روز زوج' ,'روز‌های زوج', 'روز های زوج', 'روز فرد', 'روز های فرد', 'روز‌های فرد', 'آخر هفته', 'اخر هفته', 'اخر هفته‌ها', 'اخر هفته‌ ها', 'آخر هفته‌ ها' ]
        PERIODICITY_WORDS = ['روز', 'هفته', 'روز\u200cهای', 'ساعت', 'شب' ]
        PERIODICITY_REGEX = f"(?:{DET}?{NUM}?{ADJ}?{AGG_WORDS(ANY, PERIODICITY_WORDS)}{NUM}?{ADV}?{ADJ}?{ADJECTIVES}?)"
        ASSIGNEE_WORDS = ['مسئول', 'مسئولین', 'مسئولان', 'مسئولیت']
        REMINDER_WORDS = ['یادم', 'یاداوری','یادآوری', 'باید']
        START_WORDS = ['شروع', 'استارت']
        CHANGE_WORDS = ['تغییر', 'عوض']
        CANCEL_WORDS = ['لغو', 'حذف', 'کنسل']
        CANCEL_REGEX = f"(?:{AGG_WORDS('NOUN', CANCEL_WORDS)}(?P<CANCEL>{VP}))"
        REMINDER_REGEX = f"(?:{AGG_WORDS('NOUN', REMINDER_WORDS)}(?P<REMIND>{VP}))"
        # CHANGE_REGEX = f"(?:{AGG_WORDS('NOUN', CHANGE_WORDS)}(?P<CHANGE>{VP}))"
        END_WORDS = ['پایان', 'تمام','تموم', 'انجام', 'تحویل', 'تمدید']
        PAST = ['شد', 'یافت', 'گشت', 'داده\u200cشد', 'کردم']
        PAST_VERBS = f"(?:{AGG_WORDS(ANY,PAST)})"
        TASK = f"(?:{AGG_WORDS('NOUN', TASK_WORDS)}(?P<NAME>{NP}))"
        TASK2 = f"(?:{AGG_WORDS('NOUN',REMINDER_WORDS)}(?P<REMIND>{VP}|{NOUN}){SCONJ}?{ADP}?(?P<NAME>{NP}))"
        TASKREVERSE = f"(?:{AGG_WORDS(ANY,REMINDER_WORDS)}(?P<REMIND>{VP}|{NOUN}){SCONJ}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX})(?P<NAME>{NP}))"
        TASKREVERSE2 = f"(?:{AGG_WORDS(ANY,REMINDER_WORDS)}{SCONJ}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX})(?P<NAME>{NP}))"
        TASKREVERSE3 = f"(?:{AGG_WORDS(ANY,REMINDER_WORDS)}(?P<REMIND>{VP}|{NOUN}){SCONJ}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX})(?P<START_DATE>{SAAT_REGEX}){ADP}?(?P<NAME>{NP}))"
        TASKREVERSE4 = f"(?:{AGG_WORDS(ANY,REMINDER_WORDS)}{SCONJ}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX})(?P<START_DATE>{SAAT_REGEX}){ADP}(?P<NAME>{NP}))"
        TASKREVERSE5 = f"(?:{AGG_WORDS(ANY,REMINDER_WORDS)}(?P<REMIND>{VP}|{NOUN}){SCONJ}?{ADP}?(?P<START_DATE>{SAAT_REGEX})(?P<NAME>{NP}))"
        DECLARATIONS = [
            # f"(?:{TASK}{ADP}+(?P<START_DATE>{DATETIME}){AGG_WORDS(ANY, START_WORDS)}{VERB}{ANY_T}+{ADP}+(?P<END_DATE>{DATETIME}){AGG_WORDS(ANY, END_WORDS)}{VERB})",
            # f"(?:{TASK}{ADP}?{VERB}{ADP}?(?P<START_DATE>{DATETIME}){AGG_WORDS(ANY, START_WORDS)}{VERB})",
            # f"(?:{TASK}{ADP}?{VERB}{ADP}?(?P<END_DATE>{DATETIME}){AGG_WORDS(ANY, END_WORDS)}{VERB})",
            # f"(?:(?P<ASSIGNEES>{NP_GROUP}){AGG_WORDS(ANY, ASSIGNEE_WORDS)}{TASK}{VERB})",
            # f"(?:{AGG_WORDS(ANY, ASSIGNEE_WORDS)}{TASK}{ADP}?(?P<ASSIGNEES>{NP_GROUP}){VERB})",
            f"(?:{TASKREVERSE3}{ADP}?{ADP}?{AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASKREVERSE3}{ADP}?{ADP}?{VERB})",

            f"(?:{TASKREVERSE}{ADP}?{ADP}?{AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASKREVERSE}{ADP}?{ADP}?{VERB})",
            f"(?:{TASKREVERSE2}{ADP}?{ADP}?{AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASKREVERSE2}{ADP}?{ADP}?{VERB})",
            
            f"(?:{TASKREVERSE4}{ADP}?{ADP}?{AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASKREVERSE4}{ADP}?{ADP}?{VERB})",
            f"(?:{TASKREVERSE5}{ADP}?{ADP}?{AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASKREVERSE5}{ADP}?{ADP}?{VERB})",

            

            f"(?:{TASK}{ADP}?{ADP}?{NOUN}?{ADP}?{DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}){AGG_WORDS(ANY, START_WORDS)})",
            f"(?:{TASK2}{ADP}?{ADP}?{NOUN}?{ADP}?{DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}){AGG_WORDS(ANY, START_WORDS)})",
        

            f"(?:{TASK}{ADP}?{ADP}?{NOUN}?{ADP}?{DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}))",
            f"(?:{TASK2}{ADP}?{ADP}?{NOUN}?{ADP}?{DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}))",

            f"(?:{TASK}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}){DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}){AGG_WORDS(ANY, END_WORDS)})",
            f"(?:{TASK2}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}){DAY_NIGHT}?(?P<START_DATE>{SAAT_REGEX}){AGG_WORDS(ANY, END_WORDS)})",
            f"(?:{TASK}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}){AGG_WORDS(ANY, END_WORDS)})",
            f"(?:{TASK2}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}){AGG_WORDS(ANY, END_WORDS)})",
            f"(?:{TASK}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}))",
            f"(?:{TASK2}{ADP}?{ADP}?(?P<PERIODICITY>{PERIODICITY_REGEX}))",

            

            
            
            f"(?:{TASK}{ADP}?{ADP}?{AGG_WORDS(ANY, END_WORDS)}{VERB})",

            f"(?:{TASK}{ADP}?{ADP}?)",
            f"(?:{TASK2}{ADP}?{ADP}?)",
            
            
            
            

        ]
        ASSIGNMENTS = [
            f"{AGG_WORDS(ANY, ASSIGNEE_WORDS)}{NP}*(?P<ASSIGNEES>{NP_GROUP}){VERB}",
            f"(?P<ASSIGNEES>{NP_GROUP}){AGG_WORDS(ANY, ASSIGNEE_WORDS)}{NP}*{VERB}",
        ]
        UPDATE_START_DATES = [
            f"(?:{AGG_WORDS(ANY, START_WORDS)}{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{ADP}+(?P<START_DATE>{DATETIME}){VP})",
            f"(?:{AGG_WORDS(ANY, START_WORDS)}{NP}?{AGG_WORDS('NOUN', TASK_WORDS)}{ADP}+(?P<START_DATE>{DATETIME}){VP})",
            f"(?:(?P<START_DATE>{DATETIME}){NP}?{ADP}+{AGG_WORDS(ANY, START_WORDS)}{VERB})",
            f"(?:{DET}?{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{ADP}+(?P<START_DATE>{DATETIME}){AGG_WORDS(ANY, START_WORDS)}{VERB})"
        ]
        UPDATE_DEADLINES = [
            f"(?:{AGG_WORDS(ANY, ['مهلت', 'ددلاین'])}{DET}?{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{ADP}*(?P<END_DATE>{DATETIME}){VP})",
            f"(?:{DET}?{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{ADP}+(?P<END_DATE>{DATETIME}){AGG_WORDS(ANY, END_WORDS)}{VERB})",
            f"(?:{AGG_WORDS(ANY, END_WORDS)}{DET}?{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{ADP}*(?P<END_DATE>{DATETIME}){VERB})",
        ]
        # DONES = [
        #     f"(?:{AGG_WORDS('NOUN', TASK_WORDS)}{ADP}?{NP}?{AGG_WORDS(ANY, END_WORDS)}{VERB})"
        # ]
        SUBTASK = f"(?P<SUBTASKS>{AGG_WORDS(ANY, ['ابتدا', 'اول'])}?{ANY_T}+(?:{CCONJ}{AGG_WORDS(ANY, ['سپس', 'بعد'])}{ANY_T}+)+)"
        SUBTASK_DECLARATIONS = [
            f"(?:{ADP}{NP}{VERB}{SUBTASK})",
            f"(?:{AGG_WORDS('NOUN', TASK_WORDS)}{NP}?{AGG_WORDS(ANY, ['شامل', 'متشکل'])}{ADP}?{SUBTASK}{VERB})",
        ]
        CANCELLATIONS = [f"(?:.*{CANCEL_REGEX})"]
        DONES = [f"(?:{TASK}{ADP}?.*{AGG_WORDS(ANY, END_WORDS)}{PAST_VERBS})"]
        CHANGED = [f"(?:{TASK}{ADP}?{ADP}?(?P<NEW_DATE>{SAAT_REGEX}){AGG_WORDS(ANY, CHANGE_WORDS)})"]

        def __init__(self):
            self.compiled = {}
        
        def __getitem__(self, key):
            if key not in self.compiled:
                if isinstance(self.__class__.__dict__[key], str):
                    self.compiled[key] = MixedRegexpParser(self.__class__.__dict__[key])
                else:
                    self.compiled[key] = [MixedRegexpParser(pattern) for pattern in self.__class__.__dict__[key]]
            return self.compiled[key]