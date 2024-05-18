from opsdroid.matchers import match_event
from opsdroid.skill import Skill
from opsdroid.events import Message, JoinRoom, UserInvite

class WelcomeSkill(Skill):
    @match_event(JoinRoom)
    async def welcome_user(self, invite):
        # if isinstance(invite, UserInvite):
        await invite.respond('''
سلام خوش آمدید به بات برنامه ریزی. میتوانید در این بات کارهای خود را برای انجام بدهید، آنها را تغییر بدهید.
                             کارهایتان را کنسل کنید. و لیست کارهایتان را بخواهید.
        ''')
        

