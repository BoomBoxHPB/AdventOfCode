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

    time_slots = {}
    for x in sleep_list:
        if not x[0] in time_slots:
            time_slots[x[0]] = [[x,0] for x in range(60)]
        for y in range(x[1], x[2]):
            # print(x[0])
            # print(time_slots[x[0]])
            # print(time_slots[x[0]][y])
            time_slots[x[0]][y][1] += 1
    
    slots2 = []
    for guard in list(time_slots):
        time_slots[guard].sort(key = lambda x: x[1], reverse = True)
        slots2.append([int(guard),time_slots[guard][0][0],time_slots[guard][0][1]])
    
    # print(slots2)
    slots2.sort(key = lambda x: x[2], reverse = True)

    # print(slots2[0])
    print(slots2[0][0] * slots2[0][1])
main()