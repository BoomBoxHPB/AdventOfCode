def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    positions = [int(i) for i in file.readline().strip().split(',')]
    fuel = [sum([abs(crab - i) for crab in positions]) for i in range(min(positions), max(positions) + 1)]
    print(min(fuel))

    def tri_num(i):
        return (i*(i+1))/2

    fuel = [sum([tri_num(abs(crab - i)) for crab in positions]) for i in range(min(positions), max(positions) + 1)]
    print(min(fuel))


main()
