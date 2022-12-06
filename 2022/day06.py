def puzzle(size):
    with open("./inputs/day06.txt") as f:
        content = f.read()

    for i in range(len(content)):
        if len(set(content[i : i + size])) == size:
            print(f"result position is {i + size}")
            return


# puzzle 1
puzzle(4)

# puzzle 2
puzzle(14)
