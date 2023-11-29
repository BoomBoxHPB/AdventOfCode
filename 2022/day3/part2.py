import pathlib


def calcValue(letter: str) -> int:
    value = 0
    if letter.isupper():
        value = 26
        letter = letter.lower()

    value += ord(letter) - ord("a") + 1

    return value


def run(inputPath: pathlib.Path):
    badges = []
    with inputPath.open("r") as file:
        sacks = [line.strip() for line in file.readlines()]
        for s1, s2, s3 in zip(*[iter(sacks)] * 3):
            dupe = set(s1) & set(s2) & set(s3)
            # print(dupe)

            badges.append(list(dupe)[0])

    print(sum(calcValue(letter) for letter in badges))
