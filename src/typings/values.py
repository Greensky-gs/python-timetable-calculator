import typing
from . import ids

horary = typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dayIndex = typing.Literal[1, 2, 3, 4, 5]

cours = typing.Tuple[ids.classes, str, str, horary, int, dayIndex]
day = typing.Tuple[dayIndex, typing.Tuple[cours, ...]]
week = typing.Tuple[cours, cours, cours, cours, cours]