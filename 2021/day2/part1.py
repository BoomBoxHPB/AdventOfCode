def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    directions = [l.split() for l in file.readlines()]
    for d in directions:
        d[1] = int(d[1])

    horizontal = 0
    depth = 0

    for d in directions:
        if d[0] == 'forward':
            horizontal += d[1]
        elif d[0] == 'up':
            depth -= d[1]
        elif d[0] == 'down':
            depth += d[1]

    print(f"H = {horizontal}, d = {depth}, t = {horizontal*depth}")

    horizontal = 0
    depth = 0
    aim = 0

    for d in directions:
        if d[0] == 'forward':
            horizontal += d[1]
            depth += d[1] * aim
        elif d[0] == 'up':
            aim -= d[1]
        elif d[0] == 'down':
            aim += d[1]

    print(f"H = {horizontal}, d = {depth}, t = {horizontal*depth}")

main()
