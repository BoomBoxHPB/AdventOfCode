def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    displays = []
    for line in file.readlines():
        line = line.strip()
        pattern, output = line.split('|')
        pattern = [set(list(p)) for p in pattern.split(' ')]
        output = [set(list(p)) for p in output.split(' ')]
        displays.append((pattern, output))

    count_2478 = 0
    for d in displays:
        count_2478 += sum(1 for v in d[1] if (len(v) in [2,3,4,7]))

    print(count_2478)

    # IDK, this is gonna get gross
    all_segs = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    baseline = {
        0: set('abcefg'),
        1: set('cf'),
        2: set('acdeg'),
        3: set('acdfg'),
        4: set('bdcf'),
        5: set('abdfg'),
        6: set('abdefg'),
        7: set('acf'),
        8: set('abcedfg'),
        9: set('abcdfg'),
    }
    outputs = []

    # print(baseline)

    def check_val(i, out, patterns):
        if i in out:
            return check_val(i+1, out, patterns)

        if i == 10:
            return True

        # print(out)
        for p in patterns:
            if p in out.values():
                continue

            if len(baseline[i]) == len(p):
                skip = False
                for (k,v) in out.items():
                    # print(baseline[i])
                    # print(baseline[k])
                    # print(baseline[i] & baseline[k])
                    # print(p, v, p & v)
                    if len(baseline[i] & baseline[k]) != len(p & v):
                        skip = True

                if skip:
                    continue

                out[i] = p
                if check_val(i+1, out, patterns):
                    return True
                else:
                    out.remove(i)

        return False

    totals = []
    for d in displays:
        matches = {}
        for i in [1,4,7,8]:
            matches[i] = next(v for v in d[0] if len(v) == len(baseline[i]))

        check_val(0, matches, d[0])

        # print(matches)
        multiplier = 1000
        total = 0
        for digit in d[1]:
            for (k,v) in matches.items():
                if v == digit:
                    # print(k,v)
                    total += k * multiplier
                    multiplier /= 10
                    break

        print(total)
        totals.append(total)

    print(sum(totals))

main()
