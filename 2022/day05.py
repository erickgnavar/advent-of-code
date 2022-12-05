import re
from pprint import pprint

regex = r"move (\d+) from (\d+) to (\d+)"


def prepare_data():
    res = []
    state = {}

    with open("./inputs/day05.txt") as f:
        board, moves = f.read().split("\n\n")

        flag = True
        # reverse to read from bottom to top and fill stacks
        for line in board.split("\n")[::-1]:
            if flag:
                for number in line.split("   "):
                    state[int(number)] = []
                flag = False
                continue

            i = 1
            pos = 0
            while i < 10:
                text = line[pos : pos + 4]
                match = re.search(r"\[(\w)\]", text)
                if match:
                    state[i].append(match.groups()[0])
                pos += 4
                i += 1

        pprint(state)

        # ignore base state
        for line in moves.split("\n"):
            if not line:
                continue

            res.append([int(value) for value in re.search(regex, line).groups()])
    return state, res


def puzzle1():
    state, moves = prepare_data()
    for qty, from_, to in moves:
        for _ in range(qty):
            value = state[from_].pop()
            state[to].append(value)

    last_values = []
    for key, values in state.items():
        last_values.append(values[len(values) - 1])

    print("".join(last_values))


def puzzle2():
    state, moves = prepare_data()
    for qty, from_, to in moves:
        new_values = []
        for _ in range(qty):
            value = state[from_].pop()
            new_values.append(value)

        # invert list to maintain original order
        for value in new_values[::-1]:
            state[to].append(value)
    last_values = []
    for key, values in state.items():
        last_values.append(values[len(values) - 1])

    print("".join(last_values))


puzzle1()
puzzle2()
