ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"


def evaluate(oponent, me):
    shape = 1

    if me == ROCK:
        shape = 1
    elif me == PAPER:
        shape = 2
    else:
        shape = 3

    if oponent == me:
        return shape + 3
    else:
        if me == ROCK and oponent == SCISSORS:
            return shape + 6

        elif me == PAPER and oponent == ROCK:
            return shape + 6

        elif me == SCISSORS and oponent == PAPER:
            return shape + 6
        else:
            return shape


values = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}


with open("./inputs/day02.txt") as f:
    score = 0
    for line in f.readlines():
        oponent, me = line.strip().replace("\n", "").split(" ")
        score += evaluate(values[oponent], values[me])
    print("score", score)


# X: lose
# Y: draw
# Z: win

lose = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

win = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

with open("./inputs/day02.txt") as f:
    score = 0
    for line in f.readlines():
        oponent, target = line.strip().replace("\n", "").split(" ")

        if target == "X":
            score += evaluate(values[oponent], lose[values[oponent]])
        elif target == "Y":
            score += evaluate(values[oponent], values[oponent])
        else:
            score += evaluate(values[oponent], win[values[oponent]])
    print("score", score)
