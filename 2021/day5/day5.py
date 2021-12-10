def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    lines = file.readlines()
    from_to = []
    for line in lines:
        parts = line.strip().split(' -> ')
        from_coord = parts[0].split(',')
        to_coord = parts[1].split(',')
        from_to.append((from_coord,to_coord))

    # print(from_to)
    points = {}
    for set in from_to:
        print(set)
        x1 = int(set[0][0])
        y1 = int(set[0][1])
        x2 = int(set[1][0])
        y2 = int(set[1][1])
        # print(set)

        if x1 ==x2:
            yStart = min(y1, y2)
            yEnd = max(y1, y2)
            for y in range(yStart, yEnd+1):
                addPoint(points, x1, y)
        elif y1 ==y2:
            xStart = min(x1, x2)
            xEnd = max(x1, x2)
            for x in range(xStart, xEnd+1):
                addPoint(points, x, y1)
        else: # diagonal
            xLen = abs(x1-x2)
            xInc = 1 if x2 > x1 else -1
            yInc = 1 if y2 > y1 else -1
            for i in range(xLen+1):
                addPoint(points, x1, y1)
                x1 += xInc
                y1 += yInc


    # print(points)
    overlapCount = 0
    for p in points:
        curCount = points[p]
        if curCount >= 2:
            overlapCount += 1

    print(overlapCount)

def addPoint(points, x, y):
    coord = (x,y)
    if coord not in points:
        points[coord] = 0
    points[coord] += 1
    # print(points)

main()
