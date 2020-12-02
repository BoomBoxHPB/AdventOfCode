import sys

def main():
    file = open(input("Filename: "), 'r')
    insts1 = file.readline().split(',')
    insts1 = [(i[0],int(i[1:])) for i in insts1]
    insts2 = file.readline().split(',')
    insts2 = [(i[0],int(i[1:])) for i in insts2]

    # print(insts1)
    # print(insts2)
    x = 0
    y = 0
    inst1_points = []
    for inst in insts1:
        if inst[0] == 'U':
            # print('U')
            for i in range(inst[1]):
                x = x + 1
                inst1_points.append((x,y))
        if inst[0] == 'D':
            # print('D')
            for i in range(inst[1]):
                x = x - 1
                inst1_points.append((x,y))
        if inst[0] == 'R':
            # print('R')
            for i in range(inst[1]):
                y = y + 1
                inst1_points.append((x,y))
        if inst[0] == 'L':
            # print('L')
            for i in range(inst[1]):
                y = y - 1
                inst1_points.append((x,y))
    
    x = 0
    y = 0
    inst2_points = []
    for inst in insts2:
        if inst[0] == 'U':
            # print('U')
            for i in range(inst[1]):
                x = x + 1
                inst2_points.append((x,y))
        if inst[0] == 'D':
            # print('D')
            for i in range(inst[1]):
                x = x - 1
                inst2_points.append((x,y))
        if inst[0] == 'R':
            # print('R')
            for i in range(inst[1]):
                y = y + 1
                inst2_points.append((x,y))
        if inst[0] == 'L':
            # print('L')
            for i in range(inst[1]):
                y = y - 1
                inst2_points.append((x,y))
    
    print(len(inst1_points))
    print(len(inst2_points))

    closest_point = None
    min_dist = 9999999
    for loc in inst1_points:
        current_dist = abs(loc[0]) + abs(loc[1])
        if current_dist < min_dist:
            if loc in inst2_points:
                closest_point = loc
                min_dist = current_dist
    
    print(closest_point)

main()