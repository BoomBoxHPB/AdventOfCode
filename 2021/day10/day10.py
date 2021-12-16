def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    lines = [line.strip() for line in file.readlines()]

    corrupt_scores = []
    open_c = '[{(<'
    open_to_close = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    part2_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    incomplete = []
    for line in lines:
        corrupted = False
        stack = []
        for c in line:
            if c in open_c:
                stack.append(c)
                continue

            if open_to_close[stack[-1]] == c:
                stack.pop()
            else:
                # print(''.join(stack), c)
                corrupt_scores.append(score[c])
                corrupted = True
                break

        if corrupted:
            continue

        to_fix_score = 0
        stack.reverse()
        for c in stack:
            to_fix_score *= 5
            to_fix_score += part2_score[open_to_close[c]]
        incomplete.append(to_fix_score)

    print(corrupt_scores)
    print(sum(corrupt_scores))

    print(incomplete)
    incomplete.sort()
    print(incomplete[int(len(incomplete) / 2)])


main()
