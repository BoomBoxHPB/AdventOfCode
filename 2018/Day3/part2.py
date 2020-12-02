import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    grid = [0 for x in range(1000)]
    for x in range(1000):
        grid[x] = [0 for y in range(1000)]
    double_count = 0

    #Build the grid
    for line in lines:
        words = line.split()
        x_y = words[2].split(',')
        x_y[1] = x_y[1].rstrip(':')

        dims = words[3].split('x')
        # print(line)
        # print(x_y)
        # print(dims)

        for x in range(int(x_y[0]), int(x_y[0]) + int(dims[0])):
            for y in range(int(x_y[1]), int(x_y[1]) + int(dims[1])):
                if grid[x][y] < 2:
                    grid[x][y] += 1
    
    #Check the regions to see which don't contain overlaps
    for line in lines:
        words = line.split()
        x_y = words[2].split(',')
        x_y[1] = x_y[1].rstrip(':')

        dims = words[3].split('x')
        # print(line)
        # print(x_y)
        # print(dims)

        doubled = False
        for x in range(int(x_y[0]), int(x_y[0]) + int(dims[0])):
            for y in range(int(x_y[1]), int(x_y[1]) + int(dims[1])):
                if grid[x][y] > 1:
                    doubled = True
        
        if not doubled:
            print("Step = ", words[0])
            return

    print("Double count = ", double_count)
main()