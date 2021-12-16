def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    string = file.readline().strip()
    _ = file.readline()

    rules = {}
    for line in file.readlines():
        (pair, insert) = line.strip().split(' -> ')
        rules[pair] = insert

    # Part 1 (aka This is super easy!)
    if False:
        interations = 10
        for _ in range(interations):
            new_string = string[0]
            for p in zip(string[:-1], string[1:]):
                p = ''.join(p)
                if p in rules:
                    new_string += rules[p]
                new_string += p[1]

            # print(new_string)
            string = new_string

        chars = set(string)
        count = []
        for c in chars:
            count.append(string.count(c))
        count.sort(reverse=True)
        print(count[0] - count[-1])

    # Part 2 (aka I don't have 20TB RAM)
    def add_item(dict, item, num=1):
        if item not in dict:
            dict[item] = num
        else:
            dict[item] += num

    pairs = [''.join(p) for p in zip(string[:-1], string[1:])]
    last_char = string[-1]
    pair_counts = {}
    for p in pairs:
        add_item(pair_counts,p)
    interations = 40 # 10
    # print(pair_counts)

    for _ in range(interations):
        new_pair_counts = {}
        for p,num in pair_counts.items():
            if p in rules:
                new_char = rules[p]
                add_item(new_pair_counts,p[0]+new_char, num)
                add_item(new_pair_counts,new_char+p[1], num)
            else:
                add_item(new_pair_counts,p, num)
        pair_counts = new_pair_counts
        # print(pair_counts)

    char_counts = {}
    for p,num in pair_counts.items():
        add_item(char_counts, p[0], num)
    add_item(char_counts, last_char)
    count = list(char_counts.values())
    count.sort(reverse=True)
    print(count[0] - count[-1])


main()
