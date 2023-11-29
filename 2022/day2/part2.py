import pathlib


def getScore(opponent: str, you: str) -> int:
    if you == "Rock":
        score = 1
        if opponent == "Rock":
            score += 3
        elif opponent == "Scissors":
            score += 6

    if you == "Paper":
        score = 2
        if opponent == "Paper":
            score += 3
        elif opponent == "Rock":
            score += 6

    if you == "Scissors":
        score = 3
        if opponent == "Scissors":
            score += 3
        elif opponent == "Paper":
            score += 6

    # print(score)
    return score


def getYourChoice(opp: str, outcome: str) -> str:
    # Lose
    if outcome == "X":
        if opp == "Rock":
            return "Scissors"
        if opp == "Paper":
            return "Rock"
        if opp == "Scissors":
            return "Paper"

    # Draw
    if outcome == "Y":
        return opp

    # Win
    if outcome == "Z":
        if opp == "Rock":
            return "Paper"
        if opp == "Paper":
            return "Scissors"
        if opp == "Scissors":
            return "Rock"


def run(inputPath: pathlib.Path):
    opponent = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    # you = {
    #     "X": "Rock",
    #     "Y": "Paper",
    #     "Z": "Scissors"
    # }

    total = 0

    with inputPath.open("r") as file:
        pairs = [line.strip().split() for line in file.readlines()]
        # print(pairs)
        # print([(opponent[pair[0]], you[pair[1]]) for pair in pairs])
        total = sum(
            getScore(opponent[pair[0]], getYourChoice(opponent[pair[0]], pair[1]))
            for pair in pairs
        )

    print(total)
