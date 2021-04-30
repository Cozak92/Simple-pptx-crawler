from pptx import Presentation
from hanspell import spell_checker
from hanspell.constants import CheckResult


text = ["무어신가요","맞아요","웨않대"]

for i in range(len(text)):
    result = spell_checker.check(text[i])
    print(result.as_dict())
    if result.errors > 0:
        print(result.original)