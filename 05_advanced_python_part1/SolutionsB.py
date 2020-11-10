import re
from operator import setitem
from functools import reduce


def solution1(arg):
    return [int(re.sub(r'\D', '', string)[-1::-1]) for string in arg]


def solution2(arg):
    return [i * j for i, j in arg]


def solution3(arg):
    return [i for i in filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, arg)]


def solution4(arg):
    return [item for item in filter(lambda x: x, arg)]


def solution5(arg):
    return list(map(lambda room: setitem(room, 'square', room['length'] * room['width']), arg))


def solution6(arg):
    return list(map(lambda room: dict([*room.items(), ('square', room['width'] * room['length'])]), arg))


def solution7(arg):
    return reduce(lambda x, y: x.intersection(y), arg)


def solution8(arg):
    return reduce(lambda x, y: setitem(x, y, x.get(y, 0) + 1) or x, arg, {})


def solution9(arg):
    return [student['name'] for student in
            filter(lambda x: x['gpa'] > 4.5, arg)]


def solution10(arg):
    return [lucky_ticket for lucky_ticket in
            filter(lambda num:
                   reduce(lambda x, y: -int(x) + int(y), num) == 0,
                   arg)]


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
