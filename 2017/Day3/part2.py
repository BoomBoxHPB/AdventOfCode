import queue

magic = 289326

grid = {}
future_points = queue.Queue()
curr_i = 0

(x,y) = (0,0)

grid[(x,y)] = 1

def next_point():
    global future_points
    global curr_i

    if future_points.empty():
        curr_i += 1

        # Right side
        for y in range(-curr_i+1,curr_i):
            future_points.put((curr_i,y))
        # Top side
        for x in range(curr_i,-curr_i,-1):
            future_points.put((x,curr_i))
        # Left side
        for y in range(curr_i,-curr_i,-1):
            future_points.put((-curr_i,y))
        # Bottom side
        for x in range(-curr_i,curr_i+1):
            future_points.put((x,-curr_i))

    return future_points.get()

while True:
    total = 0
    (x,y) = next_point()

    adjacent = [(x+1, y),
                (x+1, y+1),
                (x,   y+1),
                (x-1, y+1),
                (x-1, y),
                (x-1, y-1),
                (x,   y-1),
                (x+1, y-1)]
    
    for point in adjacent:
        if point in grid:
            total += grid[point]
    
    grid[(x,y)] = total

    if total > magic:
        print("First big value is",total)
        break
