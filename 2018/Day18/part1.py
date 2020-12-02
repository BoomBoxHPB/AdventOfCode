import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    # total_iterations = 10
    total_iterations = 1000000000
    grid = []

    for line in lines:
        grid.append(list(line.strip()))
    
    # need to manually initialize the first entry
    prev_grids = []
    prev_grids.append([])
    for row in range(len(grid)):
        prev_grids[0].append(list(grid[row]))

    for iteration in range(1, total_iterations + 1):
        update = [0 for x in range(len(grid))]
        for x in range(len(update)):
            update[x] = []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                curr = grid[x][y]
                # print(grid[x-1][y-1])
                if curr == '.':
                    total = 0
                    check = '|'
                    for x1 in range(max(0,x-1),1 + min(len(grid)-1,x+1)):
                        for y1 in range(max(0,y-1),1 + min(len(grid[0])-1,y+1)):
                            if (x,y) != (x1,y1) and grid[x1][y1] == check:
                                total += 1
                    if total >= 3:
                        update[x].append('|')
                    else:
                        update[x].append('.')
                elif curr == '|':
                    total = 0
                    check = '#'
                    for x1 in range(max(0,x-1),1 + min(len(grid)-1,x+1)):
                        for y1 in range(max(0,y-1),1 + min(len(grid[0])-1,y+1)):
                            if (x,y) != (x1,y1) and grid[x1][y1] == check:
                                total += 1
                    if total >= 3:
                        update[x].append('#')
                    else:
                        update[x].append('|')
                elif curr == '#':
                    tree = False
                    lumber = False
                    for x1 in range(max(0,x-1),1 + min(len(grid)-1,x+1)):
                        for y1 in range(max(0,y-1),1 + min(len(grid[0])-1,y+1)):
                            if (x,y) != (x1,y1):
                                if grid[x1][y1] == '|':
                                    tree = True
                                elif grid[x1][y1] == '#':
                                    lumber = True
                    if tree and lumber:
                        update[x].append('#')
                    else:
                        update[x].append('.')
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                grid[x][y] = update[x][y]
    
        prev_grids.append(update)
        # if iteration % 1000 == 0:
        #     print(iteration)
        #     for x in range(len(grid)):
        #         print("".join(grid[x]))
        #     print("")

        # compare to previous occurances
        for pre in range(iteration - 1, -1, -1):
            # print(pre)
            match = True
            for x in range(len(grid)):
                if grid[x] != prev_grids[pre][x]:
                    match = False
            if match:
                print("This one matches! ", iteration, pre )
                for x in range(len(prev_grids[pre])):
                    print("".join(prev_grids[pre][x]))
                print("")
                for x in range(len(grid)):
                    print("".join(grid[x]))
                print("")
                
                period = iteration - pre
                point = ( total_iterations - pre ) % period
                here = pre + point

                total_lumber = 0
                total_tree = 0

                for x in range(len(prev_grids[here])):
                    for y in range(len(prev_grids[here][x])):
                        if prev_grids[here][x][y] == '|':
                            total_tree += 1
                        elif prev_grids[here][x][y] == '#':
                            total_lumber += 1
                print("Total resource value = ", total_tree * total_lumber)
                return

        # print("")

    # for pre in range(len(prev_grids)):
    #     for x in range(len(prev_grids[pre])):
    #         print("".join(prev_grids[pre][x]))
    #     print("")

    # for x in range(len(grid)):
    #     print("".join(grid[x]))
    # print("")

main()