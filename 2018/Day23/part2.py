import sys

def main():
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    bots = []

    for line in lines:
        parts = line.split(',')
        loc = []
        loc.append(int(parts[0].strip('pos=<>')))
        loc.append(int(parts[1].strip("pos=<>")))
        loc.append(int(parts[2].strip("pos=<>")))
        r = int(parts[3].strip(" r=\n"))
        bots.append((loc,r))
    
    bots.sort(key = lambda x: x[0][0])
    x_range = (bots[0][0][0], bots[len(bots)-1][0][0])
    print(x_range)

    bots.sort(key = lambda x: x[0][1])
    y_range = (bots[0][0][1], bots[len(bots)-1][0][1])
    print(y_range)

    bots.sort(key = lambda x: x[0][2])
    z_range = (bots[0][0][2], bots[len(bots)-1][0][2])
    print(z_range)

    max_in_range = 0
    potential_points = []
    for x in range(x_range[0], x_range[1]+1):
        # print("x=", x)
        for y in range(y_range[0], y_range[1]+1):
            # print("y=", y)
            for z in range(z_range[0], z_range[1]+1):
                in_range = 0
                for b in range(len(bots)):
                    d  = abs(x - bots[b][0][0])
                    d += abs(y - bots[b][0][1])
                    d += abs(z - bots[b][0][2])
                    if d <= bots[b][1]:
                        in_range += 1
                if in_range > max_in_range:
                    # print(max_in_range, in_range)
                    max_in_range = in_range
                    potential_points = [(x,y,z)]
                elif in_range == max_in_range:
                    potential_points.append((x,y,z))

    # print(max_in_range)
    # print(potential_points)
    closest_d = 1000000000
    closest_point = 0
    for x in potential_points:
        d = x[0] + x[1] + x[2]
        if d < closest_d:
            closest_point = x
    
    print(x)

main()