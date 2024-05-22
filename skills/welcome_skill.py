from opsdroid.skill import Skill
from opsdroid.matchers import match_event
from opsdroid.events import JoinRoom, Message

class WelcomeSkill(Skill):
    @match_event(JoinRoom)
    async def welcome(self, opsdroid):
        await opsdroid.respond(Message(text='''
سلام خوش آمدید به بات برنامه ریزی. میتوانید در این بات برای انجام کارهای خود برنامه ریزی بکنید، برنامه آنها را تغییر بدهید.
                             برنامه کارهایتان را کنسل کنید. و لیست کارهایتان در یک بازه دلخواه را بخواهید را بخواهید.
'''))