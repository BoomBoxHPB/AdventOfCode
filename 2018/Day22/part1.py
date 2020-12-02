import sys

def main():
    depth = 5616
    target = (10,785)

    # test case
    # depth = 510
    # target = (10,10)
    total_risk = 0

    grid = [0 for x in range(target[1] + 1)]
    for x in range(len(grid)):
        grid[x] = [0 for y in range(target[0] + 1)]
    
    print(len(grid), len(grid[0]))

    grid[0][0] = 0
    for y in range(1, len(grid)):
        grid[y][0] = ((y * 48271) + depth ) % 20183
    
    for x in range(1, len(grid[0])):
        grid[0][x] = ((x * 16807) + depth) % 20183

    for y in range(1, len(grid)):
        for x in range(1, len(grid[0])):
            grid[y][x] = ((grid[y-1][x] * grid[y][x-1]) + depth ) % 20183
    
    # Target geological index is always 0
    grid[target[1]][target[0]] = (depth % 20183)

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            total_risk += grid[y][x] % 3
    
    print(grid[0][1])
    print(grid[1][0])
    print(grid[1][1])
    print(grid[10][10])

    print(total_risk)

main()