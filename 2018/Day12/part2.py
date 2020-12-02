import sys
def main():
    file = open(sys.argv[1], 'r')
    init_list = list(file.readline().strip().split()[2])
    pots = []
    prev_pots = []
    rules = {}
    time_length = 300

    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break
        parts = line.strip().split()
        rules[parts[0]] = parts[2]

    offset = 3
    for x in range(offset):
        pots.append('.')
    for x in range(len(init_list)):
        pots.append(init_list[x])
    for x in range(offset):
        pots.append('.')

    # print(rules)
    for x in range(time_length):
        print("".join(pots))
        prev_pots.append(list(pots))
        new_pots = ['.','.']
        for y in range(len(pots)-4):
            # print(pots[y:y+5])

            # hack for the test case
            entry = "".join(pots[y:y+5])
            if not entry in rules:
                rules[entry] = '.'

            new_pots.append(rules[entry])

        if new_pots[len(new_pots) - 1] == '#':
            new_pots.append('.')
        new_pots.append('.')
        new_pots.append('.')

        if new_pots[2] == '#':
            new_pots.insert(0, '.')
            offset += 1
        elif new_pots[3] == '.':
            new_pots.remove('.')
            offset -= 1
        
        pots = list(new_pots)

        if x % 1000== 0:
            print(x)
        # if new_pots in prev_pots:
        #     print("Found a dupe, ", x, prev_pots.index(new_pots))
        #     break
    
    print("".join(pots))

    total = 0
    for x in range(len(pots)):
        if pots[x] == '#':
            total += x - offset
            print(x-offset)

    print(total)
main()