def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    matrix = []
    for line in file.readlines():
        matrix.append([int(i) for i in line.strip()])

    print(matrix)

    def getVal(i,j):
        if i < 0 or j < 0:
            return 9
        try:
            return matrix[i][j]
        except IndexError:
            return 9

    basins = []
    def checkBasin(i, j, basin):
        points = [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
        for p in points:
            skip = False
            for b in basins:
                if p in b:
                    skip = True
                    break

            if skip:
                continue

            if p not in basin and 9 != getVal(p[0],p[1]):
                # print(p, getVal(p[0],p[1]))
                basin.append(p)
                checkBasin(p[0], p[1], basin)

    low_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = getVal(i,j)
            adj = []
            adj.append(getVal(i+1,j))
            adj.append(getVal(i,j+1))
            adj.append(getVal(i,j-1))
            adj.append(getVal(i-1,j))

            # Change to strictly less-than for part 1
            if all(val < v for v in adj):
                # print(i, j)
                low_points.append(val)
                basin = [(i,j)]
                checkBasin(i, j, basin)
                basins.append(basin)

    print(sum(low_points) + len(low_points))

    basin_total = 1
    basins.sort(key=len, reverse=True)
    # for b in basins:
    #     print(b)
    for b in basins[:3]:
        basin_total *= len(b)
    print(basin_total)

main()
