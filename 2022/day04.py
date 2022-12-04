import re


line_regex = r"(\d+)-(\d+),(\d+)-(\d+)"


def puzzle1():
    with open("./inputs/day04.txt") as f:
        res = 0
        for line in f.readlines():
            [start1, end1, start2, end2] = [
                int(value) for value in re.search(line_regex, line).groups()
            ]
            group1 = set(range(start1, end1 + 1))
            group2 = set(range(start2, end2 + 1))
            if group1.issubset(group2) or group2.issubset(group1):
                res += 1
        print(f"puzzle 1: {res}")


def puzzle2():
    with open("./inputs/day04.txt") as f:
        res = 0
        for line in f.readlines():
            [start1, end1, start2, end2] = [
                int(value) for value in re.search(line_regex, line).groups()
            ]
            group1 = set(range(start1, end1 + 1))
            group2 = set(range(start2, end2 + 1))
            if group1.intersection(group2):
                res += 1
        print(f"puzzle 2: {res}")


puzzle1()
puzzle2()
