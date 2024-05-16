from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from task_extractor.extractor import TaskExtractor

class HelloSkill(Skill):
    @match_regex(r'.*')
    async def hello(self, message):

        # await message.respond('Hey, I love Alireza Amiri!')
        print("Pending")
        extractor = TaskExtractor()
        extractor.run(str(message))
        await message.respond(str(extractor.tasks))
