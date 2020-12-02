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
    
    bots.sort(key = lambda x: x[1], reverse = True)
    # print(bots)
    
    in_range = 0
    for x in range(len(bots)):
        d  = abs(bots[0][0][0] - bots[x][0][0])
        d += abs(bots[0][0][1] - bots[x][0][1])
        d += abs(bots[0][0][2] - bots[x][0][2])
        if d <= bots[0][1]:
            in_range += 1

    print(in_range)


main()