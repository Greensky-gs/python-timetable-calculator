from typing import Literal, Union, get_args
from utils.toolbox import flatten

level = Literal["sc", "pr", 'te']
classes = Literal["maths", "physics", "nsi", "hlp", "hggsp", "chinese", "german", "english", "french", "eps", "ses", "history", "emc", "japanese"]
lang = Literal["chinese", "english", "german", "japanese"]
option = Literal["chinese_lv3", "japanese_lv3", "euro_english"]

allClasses = Union[classes, lang, option]
allClassesStr = flatten(list(map(lambda x: get_args(x), get_args(allClasses))))
levelStr = get_args(level)
langStr = get_args(lang)
classesStr = get_args(classes)
optionStr = get_args(option)