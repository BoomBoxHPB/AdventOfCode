import sys
import math

magic = 289326
# magic = 1
# magic = 12
# magic = 23
# magic = 1024

total_w = 1

while magic > (total_w*total_w):
    total_w += 1

print( "width = ", total_w)

start = int(math.pow((total_w-1),2))
# print(start)

(x,y) = (int(total_w/2),int(total_w/2))
# print(x,y)

corner_v = math.pow(total_w,2) - (total_w-1)
print(corner_v)

if magic < corner_v:
    delta = corner_v - magic
    y -= delta
elif magic > corner_v:
    delta = magic - corner_v
    x -= delta

dist = abs(x) + abs(y)
print(dist)