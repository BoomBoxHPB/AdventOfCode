import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()

    lines.sort()

    # print(lines)

    # Want minute, guard/wake/falls, #XX
    parsed_lines = []
    for line in lines:
        output = [0 for x in range(3)]
        temp = line.split()
        output[0] = int(temp[1].strip(']').split(':')[1]) #minute time
        output[1] = temp[2]
        output[2] = temp[3].strip('#')
        parsed_lines.append(list(output))

    # print(parsed_lines)

    sleep_list = []
    current_guard = 0
    sleep_time = 0
    for x in parsed_lines:
        if x[1] == "Guard":
            current_guard = x[2]
        elif x[1] == "falls":
            sleep_time = x[0]
        elif x[1] == "wakes":
            sleep_list.append((current_guard, sleep_time, x[0]))

    # print(sleep_list)

    total = []
    for x in sleep_list:
        this_one = 0
        for y in total:
            if y[0] == x[0]:
                this_one = y
                break
        if this_one != 0:
            this_one[1] += x[2] - x[1]
        else:
            total.append([x[0], x[2] - x[1]])

    print(total)
    total.sort(key = lambda x: x[1], reverse = True)

    print(total[0][0])

    time_slots = [[x,0] for x in range(60)]
    for x in sleep_list:
        if x[0] == total[0][0]:
            for y in range(x[1], x[2]):
                time_slots[y][1] += 1
    
    time_slots.sort(key = lambda x: x[1], reverse = True)
    print(time_slots[0])

    print(time_slots[0][0] * int(total[0][0]))
main()