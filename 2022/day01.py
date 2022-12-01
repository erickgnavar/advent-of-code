def clean_and_group(path):
    res = []
    with open(path) as f:
        raw_text = f.read()
        # groups of calories are separated by a blank space
        for group in raw_text.split("\n\n"):
            calories = [int(value) for value in group.split("\n") if value.isdigit()]
            res.append(calories)
    return res


def get_max_calories(groups):
    return max([sum(values) for values in groups])


def get_top_3(groups):
    sums = [sum(values) for values in groups]
    ordered = sorted(sums, reverse=True)
    return ordered[:3]


input_path = "./inputs/day01.txt"
groups = clean_and_group(input_path)
max_calories = get_max_calories(groups)
print(f"Max calories: {max_calories}")

top_3 = get_top_3(groups)
print(f"top 3: {top_3}")

print(f"sum top 3: {sum(top_3)}")
