import sys

def main():
    # file = open(sys.argv[1], 'r')
    # lines = file.readlines()

    grid_serial = 9995
    grid = [0 for x in range(300)]
    for x in range(300):
        grid[x] = [0 for y in range(300)]

    for x in range(300):
        for y in range(300):
            rack_id = x + 1 + 10
            pwr_lvl = rack_id * (y + 1)
            pwr_lvl += grid_serial
            pwr_lvl *= rack_id
            pwr_lvl = int( pwr_lvl / 100 ) % 10
            pwr_lvl -= 5

            grid[x][y] = pwr_lvl
    
    # print(grid[2][4])

    max_power = 0 # probably isn't the max
    max_xy = (0,0)
    max_s = 0

    for s in range(1,301):
        print("size = ", s)
        row_pwr = [0 for x in range(301 - s)]
        for x in range(301 - s):
            row_pwr[x] = [0 for y in range(300)]
            for y in range(300):
                for i in range(s):
                    row_pwr[x][y] += grid[x+i][y]
        # TODO - calculate the sum of each row given the size
        # then just use those sums rather than duplicating the
        # work every row.
        for x in range(301 - s):
            for y in range(301 - s):
                pwr_sum = 0
                for i in range(s):
                    # print(y+i, len(row_pwr[x]))
                    pwr_sum += row_pwr[x][y+i]

                if pwr_sum > max_power:
                    max_power = pwr_sum
                    max_s = s
                    max_xy = (x+1, y+1)
    
    # print(grid[32][44], grid[33][44], grid[34][44])
    # print(grid[32][45], grid[33][45], grid[34][45])
    # print(grid[32][46], grid[33][46], grid[34][46])
    print("Max x,y,size = ", max_xy, max_s)
    print(max_power)

main()