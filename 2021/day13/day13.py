def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    lines = [line.strip() for line in file.readlines()]
    points = set()
    folds = []
    for line in lines:
        if line == '':
            continue

        if line.startswith('fold'):
            (dir,loc) = line.removeprefix('fold along ').split('=')
            folds.append((dir,int(loc)))
        else:
            (x,y) = line.split(',')
            points.add((int(x),int(y)))

    print(points)
    print(folds)

    first_fold = True
    for fold in folds:
        dir = fold[0]
        line = fold[1]

        new_points = set()
        for p in points:
            if dir == 'x' and p[0] > line:
                new_points.add((abs(p[0]-(2*line)), p[1]))
            elif dir == 'y' and p[1] > line:
                new_points.add((p[0], abs(p[1]-(2*line))))
            else:
                new_points.add(p)
        points = new_points

        if first_fold:
            print(len(points))
            first_fold = False

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(max_y + 1):
        string = ''
        for x in range(max_x + 1):
            if (x,y) in points:
                string += '#'
            else:
                string += ' '
        print(string)




main()
