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

    for x in range(300 - 2):
        for y in range(300 - 2):
            pwr_sum = grid[x][y] + grid[x+1][y] + grid[x+2][y]
            pwr_sum += grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1]
            pwr_sum += grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2]

            if pwr_sum > max_power:
                max_power = pwr_sum
                max_xy = (x+1, y+1)
    
    # print(grid[32][44], grid[33][44], grid[34][44])
    # print(grid[32][45], grid[33][45], grid[34][45])
    # print(grid[32][46], grid[33][46], grid[34][46])
    print("Max x,y = ", max_xy)
    print(max_power)

main()