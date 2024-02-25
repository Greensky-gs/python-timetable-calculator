import typing
from . import ids
from . import values

specialities = typing.Tuple[ids.classes, str]
langs = typing.Tuple[ids.lang, str]
options = typing.Tuple[ids.option, str]
disponibility = typing.Tuple[values.dayIndex, typing.Tuple[values.horary, ...]]
disponibilities = typing.Tuple[disponibility, disponibility, disponibility, disponibility, disponibility]

student = typing.Tuple[str, ids.level, str, str, specialities, specialities, specialities, langs, langs, options, options, options, str, str]
teacher = typing.Tuple[str, typing.Tuple[ids.allClasses, ...], disponibilities, str, typing.Tuple[str, ...]]