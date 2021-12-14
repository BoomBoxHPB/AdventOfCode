def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')
    raw_fishes = [int(i) for i in file.readline().strip().split(',')]

    # print(raw_fishes)
    fishes = {}
    for i in range(-1, 9):
        fishes[i] = 0

    for age in raw_fishes:
        fishes[age] += 1

    # print(fishes)

    part1_len = 80
    part2_len = 256

    for i in range(part2_len):
        for j in range(9):
            fishes[j-1] = fishes[j]

        fishes[8] = fishes[-1]
        fishes[6] += fishes[-1]
        fishes[-1] = 0

    total_fishes = sum([v for k,v in fishes.items()])
    print(total_fishes)

main()
