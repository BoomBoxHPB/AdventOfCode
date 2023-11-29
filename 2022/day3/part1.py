import pathlib

def calcValue(letter: str) -> int:
    value = 0
    if letter.isupper():
        value = 26
        letter = letter.lower()

    value += ord(letter) - ord('a') + 1

    return value

def run(inputPath: pathlib.Path):
    dupes = []
    with inputPath.open('r') as file:
        sacks = [line.strip() for line in file.readlines()]
        for sack in sacks:
            center = int(len(sack) / 2)
            compartments = (set(sack[:center]),set(sack[center:]))
            # print(compartments)
            dupe = compartments[0] & compartments[1]
            # print(dupe)
            dupes.append(list(dupe)[0])
    

    print(sum(calcValue(letter) for letter in dupes))