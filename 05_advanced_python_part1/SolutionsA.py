def solution1(arg):
    return [letter * 4 for letter in arg]


def solution2(arg):
    return [letter * (i + 1) for i, letter in enumerate(arg)]


def solution3(arg):
    return [i for i in arg if i % 3 == 0 or i % 5 == 0]


def solution4(arg):
    return [item
            for lst in arg
            for item in lst]


def solution5(arg):
    return [(a, b, c)
            for a in range(1, arg + 1)
            for b in range(a, arg + 1)
            for c in range(b, arg + 1)
            if (a * a + b * b) == c * c]


def solution6(arg):
    return [[i + j for j in arg[1]] for i in arg[0]]


def solution7(arg):
    return [[row[i] for row in arg] for i in range(len(arg[0]))]


def solution8(arg):
    return [[int(digit) for digit in word.split()] for word in arg]


def solution9(arg):
    return {chr(i + ord('a')): i ** 2 for i in arg}


def solution10(arg):
    return {name.title() for name in arg if len(name) > 3}


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
