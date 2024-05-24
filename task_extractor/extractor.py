import json
import hazm
from task_extractor.patterns import Patterns
import re
from task_extractor.parser import MixedRegexpParser

class Task:
    def __init__(self):
        self.name = ''
        self.time = ''
        self.periodicity = ''
        self.is_done = False
        self.is_cancelled = False
        self.task_type = 'add'

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)
    
class Event:
    def __init__(self):
        self.name = ''
        self.start_date = ''
        self.end_date = ''
        self.new_date = ''
        self.is_done = False
        self.is_cancelled = False

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)

class TaskExtractor:
    normalizer = hazm.Normalizer()
    sent_tokenizer = hazm.SentenceTokenizer()
    word_tokenizer = hazm.WordTokenizer()
    POS_tagger = hazm.POSTagger(model='models/pos_tagger.model')
    lemmatizer = hazm.Lemmatizer()
    patterns = Patterns()

    def __init__(self):
        self.tasks = []
    
    def check_for_tasks(self, name):
        for task in self.tasks:
            if task.name.startswith(name) or name.startswith(task.name):
                return True
        return False
    
    def parse_name(self, groups):
        if 'NAME' in groups:
            if self.check_for_tasks(' '.join(word for word, tag in groups['NAME'])):
                return None
            return ' '.join(word for word, tag in groups['NAME'])
    
    def parse_start_date(self, task, groups):
        if 'START_DATE' in groups:
            task.time = ' '.join(word for word, tag in groups['START_DATE'])

    def parse_new_date(self, task, groups):
        if 'NEW_DATE' in groups:
            
            task.time = ' '.join(word for word, tag in groups['NEW_DATE'])

    def parse_period(self, task, groups):

        if 'PERIOD' in groups:
            task.time = ' '.join(self.lemmatizer.lemmatize(word) for word, tag in groups['PERIOD'])

    def normalize_period(self, periodicity):
        if periodicity == 'هر روز' or periodicity == 'هرروز':
            periodicity = 'روزانه'
        elif periodicity == 'هر هفته' or periodicity == 'هرهفته':
            periodicity = 'هفتگی'
        elif periodicity == 'هر ماه' or periodicity == 'هرماه':
            periodicity = 'ماهانه'
        elif periodicity == 'هر سال' or periodicity == 'هرسال':
            periodicity = 'سالانه'
        return periodicity   
            

    def parse_periodicity(self, task, groups):
        if 'PERIODICITY' in groups:
            task.periodicity = ' '.join(self.lemmatizer.lemmatize(word) for word, tag in groups['PERIODICITY'])
    
    def parse_end_date(self, task, groups):
        if 'END_DATE' in groups:
            task.end_date = ' '.join(word for word, tag in groups['END_DATE'])
    

    
    

    def run(self, text: str) -> list[Task]:
        text = self.normalizer.normalize(text)
        for sent in self.sent_tokenizer.tokenize(text):
            words = self.word_tokenizer.tokenize(sent)
            tags = self.POS_tagger.tag(words)
            tags = [tag for tag in tags if tag[1] != 'PUNCT']

            

            for pattern in self.patterns['DECLARATIONS']:
                result = pattern.parse(tags)
                # print(tags)
                # print(result)
                if result:
                    matches, groups = result
                    name = self.parse_name(groups)
                    if not name:
                        continue
                    task = Task()
                    task.name = name
                    self.parse_start_date(task, groups)
                    self.parse_end_date(task, groups)
                    self.parse_periodicity(task, groups)
                    self.tasks.append(task)
                    break

            
                
            if not self.tasks:
                for pattern in self.patterns['RETURNS']:
                    result = pattern.parse(tags)
                    # print(tags)
                    # print(result)
                    if result:
                        matches, groups = result
                        task = Task()
                        self.parse_period(task, groups)
                        self.tasks.append(task)
                        task.task_type = "return"
                        break
                

            if not self.tasks:
                continue


            

            for pattern in self.patterns['CANCELLATIONS']:
                result = pattern.parse(tags)
                if result:
                    task.task_type = 'cancelation'
                    task.is_cancelled = True


            for pattern in self.patterns['DONES']:
                result = pattern.parse(tags)
                if result:
                    task.task_type = 'done'
                    task.is_done = True

            for pattern in self.patterns['CHANGED']:
                result = pattern.parse(tags)
                # print(result)
                if result:
                    matches, groups = result
                    self.parse_new_date(self.tasks[-1], groups)
                    task.task_type = 'change'
                    break
                    

            for pattern in self.patterns.DONES:
                result = MixedRegexpParser(pattern).parse(tags)
                if result:
                    matches, groups = result
                    self.tasks[-1].is_done = True

        for task in self.tasks:
            task.periodicity = self.normalize_period(task.periodicity)
            task.time = self.normalize_period(task.time)
        return self.tasks
    