import sys
def main():
    file = open(sys.argv[1], 'r')
    init_list = list(file.readline().strip().split()[2])
    pots = []
    rules = {}
    time_length = 20

    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break
        parts = line.strip().split()
        rules[parts[0]] = parts[2]

    offset = time_length + 3
    for x in range(offset):
        pots.append('.')
    for x in range(len(init_list)):
        pots.append(init_list[x])
    for x in range(offset):
        pots.append('.')

    # print(rules)
    for x in range(time_length):
        print("".join(pots))
        new_pots = ['.','.']
        for y in range(len(pots)-4):
            # print(pots[y:y+5])

            # hack for the test case
            entry = "".join(pots[y:y+5])
            if not entry in rules:
                rules[entry] = '.'

            new_pots.append(rules[entry])
        new_pots.append('.')
        new_pots.append('.')
        # print(len(pots))
        # print(len(new_pots))
        # print("".join(pots))
        # print("".join(new_pots))

        pots = list(new_pots)
    
    print("".join(pots))

    total = 0
    for x in range(len(pots)):
        if pots[x] == '#':
            total += x - offset
            print(x-offset)

    print(total)
main()