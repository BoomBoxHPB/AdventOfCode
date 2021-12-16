def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    matrix = [[int(i) for i in line.strip()] for line in file.readlines()]
    # print(matrix)

    iterations = 9999999

    def increment_val(point):
        if point[0] < 0 or point[1] < 0:
            return
        try:
            old_val = get_val(point)
            set_val(point, old_val + 1)
        except IndexError:
            return


    def get_val(point):
        return matrix[point[0]][point[1]]

    def set_val(point, val):
        matrix[point[0]][point[1]] = val

    def increment_adjacent(point):
        adj = [
            ( 1,-1), ( 1, 0), ( 1, 1),
            ( 0,-1),          ( 0, 1),
            (-1,-1), (-1, 0), (-1, 1),
        ]

        for a in adj:
            p = (point[0] + a[0], point[1] + a[1])
            # print(point, a, p)
            increment_val(p)

    num_flashes = []
    for x in range(iterations):
        # Initial increment
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                increment_val((i,j))

        # for m in matrix:
        #     print(m)
        # print('')

        # Handle explosions
        explosion = True
        exploded = []
        while explosion:
            explosion = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    point = (i,j)
                    if get_val(point) > 9 and point not in exploded:
                        explosion = True
                        exploded.append(point)
                        increment_adjacent(point)

        # for m in matrix:
        #     print(m)
        # print('')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                point = (i,j)
                if get_val(point) > 9:
                    set_val(point, 0)

        num_flashes.append(len(exploded))

        # for m in matrix:
        #     print(m)
        # print('')

        # Check for zeros
        if all(all(p == 0 for p in line) for line in matrix):
            print("Zeros at {}".format(x+1))
            return



    print(num_flashes)
    print(sum(num_flashes))





main()
