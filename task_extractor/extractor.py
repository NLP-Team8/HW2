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
            
            task.new_date = ' '.join(word for word, tag in groups['NEW_DATE'])
            task.time = task.new_date

    def parse_periodicity(self, task, groups):
        if 'PERIODICITY' in groups:
            task.periodicity = ' '.join(word for word, tag in groups['PERIODICITY'])
    
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
            if not self.tasks:
                continue
            for pattern in self.patterns['ASSIGNMENTS'] + self.patterns['UPDATE_START_DATES'] + self.patterns['UPDATE_DEADLINES'] + self.patterns['SUBTASK_DECLARATIONS']:
                result = pattern.parse(tags)
                if result:
                    matches, groups = result
                    self.parse_periodicity(self.tasks[-1], groups)
                    self.parse_start_date(self.tasks[-1], groups)
                    self.parse_end_date(self.tasks[-1], groups)

            for pattern in self.patterns['CANCELLATIONS']:
                result = pattern.parse(tags)
                if result:
                    task.is_cancelled = True


            for pattern in self.patterns['DONES']:
                result = pattern.parse(tags)
                if result:
                    task.is_done = True

            for pattern in self.patterns['CHANGED']:
                result = pattern.parse(tags)
              
                if result:
                    matches, groups = result
               
                    self.parse_new_date(self.tasks[-1], groups)
                    

            for pattern in self.patterns.DONES:
                result = MixedRegexpParser(pattern).parse(tags)
                if result:
                    matches, groups = result
                    self.tasks[-1].is_done = True
        return self.tasks
    
class EventExtractor:
    normalizer = hazm.Normalizer()
    sent_tokenizer = hazm.SentenceTokenizer()
    word_tokenizer = hazm.WordTokenizer()
    POS_tagger = hazm.POSTagger(model='models/pos_tagger.model')
    lemmatizer = hazm.Lemmatizer()
    patterns = Patterns()

    def __init__(self):
        self.events = []

    def parse_event_name(self, groups):
        return ' '.join(word for word, tag in groups['NAME'])

    def parse_datetime(self, event, groups, date_type):
        if date_type in groups:
            datetime_str = ' '.join(word for word, tag in groups[date_type])
            setattr(event, date_type, datetime_str)
        else:
            setattr(event, date_type, None)

    def parse_period(self, event, groups):
        event.period = ' '.join(word for word, tag in groups['PERIODICITY'])

    def run(self, text: str) -> list[Event]:
        text = self.normalizer.normalize(text)
        sentences = self.sent_tokenizer.tokenize(text)
        for sentence in sentences:
            print(sentence)
            words = self.word_tokenizer.tokenize(sentence)
            tags = self.POS_tagger.tag(words)
            tags = [tag for tag in tags if tag[1] != 'PUNCT']

            for pattern_type in ['DECLARATIONS', 'ASSIGNMENTS', 'UPDATE_START_DATES', 'UPDATE_DEADLINES', 'CANCELLATIONS', 'DONES']:
                for pattern in self.patterns[pattern_type]:
                    result = pattern.parse(tags)
                    print(pattern)
                    if result:
                        matches, groups = result
                        event = Event()
                        if 'NAME' in groups:
                            event.name = self.parse_event_name(groups)
                        if 'START_DATE' in groups:
                            self.parse_datetime(event, groups, 'START_DATE')
                        if 'END_DATE' in groups:
                            self.parse_datetime(event, groups, 'END_DATE')
                        if 'PERIODICITY' in groups:
                            self.parse_period(event, groups)
                        if pattern_type == 'DONES':
                            event.is_done = True
                        if pattern_type == 'CANCELLATIONS':
                            event.is_cancelled = True
                        self.events.append(event)
        return self.events