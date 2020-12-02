import sys

steps = open(sys.argv[1], 'r').readline().split(',')
dirs = {}
dirs['n']  = (1,0,-1)
dirs['ne'] = (0,1,-1)
dirs['se'] = (-1,1,0)
dirs['s']  = (-1,0,1)
dirs['sw'] = (0,-1,1)
dirs['nw'] = (1,-1,0)

point = (0,0,0)
max_dist = 0

for step in steps:
    point = tuple(sum(x) for x in zip(point, dirs[step]))
    max_dist = max(max_dist,max((abs(min(point)),max(point))))

print(point)
print(max(abs(min(point)),max(point)))
print(max_dist)