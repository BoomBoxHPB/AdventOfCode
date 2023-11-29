import pathlib

def run(inputPath: pathlib.Path):
    elfs = []
    with inputPath.open('r') as file:
        input = [line.strip() for line in file.readlines()]
    
    currentElf = 0
    for cal in input:
        if not cal:
            elfs.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(cal)
    if currentElf:
        elfs.append(currentElf)
    
    elfs.sort()
    # print(elfs)
    print(sum(elfs[-3:]))