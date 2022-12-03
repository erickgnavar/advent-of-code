def calculate_priority_1(line):
    size = len(line)
    part1 = set(line[: int(size / 2)])
    part2 = set(line[int(size / 2) :])
    letter = list(part1.intersection(part2))[0]
    if letter.islower():
        # priority for lowercase start at 1
        return ord(letter) - 96
    else:
        # priority for uppercase start at 27
        return ord(letter) - 38


def calculate_priority_2(group1, group2, group3):
    group1 = set(group1)
    group2 = set(group2)
    group3 = set(group3)
    letter = list(group1.intersection(group2.intersection(group3)))[0]

    if letter.islower():
        # priority for lowercase start at 1
        return ord(letter) - 96
    else:
        # priority for uppercase start at 27
        return ord(letter) - 38


def puzzle1():
    with open("./inputs/day03.txt") as f:
        res = 0
        for line in f.readlines():
            res += calculate_priority_1(line)
        print(f"puzzle 1: {res}")


def puzzle2():
    with open("./inputs/day03.txt") as f:
        res = 0
        lines = [line.replace("\n", "") for line in f.readlines()]
        groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]

        for g1, g2, g3 in groups:
            res += calculate_priority_2(g1, g2, g3)

        print(f"puzzle 2: {res}")


puzzle1()
puzzle2()
