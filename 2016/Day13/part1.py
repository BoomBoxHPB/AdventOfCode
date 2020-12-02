import sys
import queue

magic = 1362 #10
end = [31,39] #[7,4] 

def is_wall(x,y):
    t = (x*x) + (3*x) + (2*x*y) + y + (y*y)
    t += magic

    bits = 0
    while t != 0:
        if t & 1:
            bits += 1
        t = t >> 1
    
    if bits & 1 == 1:
        return True
    else:
        return False

def bfs(x,y):
    traversed = {}
    q = queue.Queue()

    q.put((x,y,0))

    while not q.empty():
        (x,y,d) = q.get()

        if (x,y) in traversed:
            continue

        if x == end[0] and y == end[1]:
            return d
        
        if is_wall(x,y):
            continue

        traversed[(x,y)] = True

        if x > 0:
            q.put((x-1,y,d+1))
        if y > 0:
            q.put((x,y-1,d+1))
        q.put((x+1,y,d+1))
        q.put((x,y+1,d+1))
        
    return -1

print("Distance: ",bfs(1,1))