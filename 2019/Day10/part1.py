import sys
import math

# get angle from "up" in 0 to 2pi
def get_angle(pointA, pointB):
    rise = pointB[1] - pointA[1]
    run = pointB[0] - pointA[0]
    slope = math.atan2(rise, run)

    # rotate back to reference Y axis
    slope += math.pi/2

    #normalize to 0 to 2pi
    while slope < 0:
        slope += math.pi * 2
    while slope >= ( math.pi * 2 ):
        slope -= math.pi * 2

    # print(pointA, pointB, rise, run, slope)

    return slope

def main():
    f = open(input("Filename: "), 'r')
    lines = f.readlines()

    asteroids = []
    rowCount = 0
    for row in lines:
        colCount = 0
        for char in row:
            if char == "#":
                asteroids.append( [(colCount, rowCount), 0] )
            colCount += 1
        rowCount += 1

    for asteroid in asteroids:
        # currLoc = (2,2)
        currLoc = asteroid[0]

        slopes = []
        for other in asteroids:
            otherLoc = other[0]
            if currLoc == otherLoc:
                continue
            
            slope = get_angle(currLoc, otherLoc)
            if slope not in slopes:
                asteroid[1] += 1
                slopes.append( slope )
        # break

    # print( asteroids )

    print( max( asteroids, key=lambda x:x[1] ) )

main()