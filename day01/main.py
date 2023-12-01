import re

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find(line, range, replacements):
    for i in range:
        if line[i : i + 1].isnumeric():
            return line[i : i + 1]
        for key, value in replacements.items():
            if re.match(r"^{}".format(key), line[i:], flags=re.M):
                return value


def get_number(line, replacements):
    line_range = range(len(line))
    num_one = find(line, line_range, replacements)
    num_two = find(line, reversed(line_range), replacements)
    return int(num_one + num_two)


with open("./input") as input:
    lines = input.readlines()
    part_one = map(lambda l: get_number(l, {}), lines)
    part_two = map(lambda l: get_number(l, replacements), lines)
    print("Part one:", sum(part_one))
    print("Part two:", sum(part_two))
