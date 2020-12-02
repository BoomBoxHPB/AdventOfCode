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

def get_dist(pointA, pointB):
    rise = pointB[1] - pointA[1]
    run = pointB[0] - pointA[0]
    return math.sqrt(rise*rise + run*run)

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
        
        asteroid.append(slopes)
        # break

    # print( asteroids )

    base = max( asteroids, key=lambda x:x[1] )
    slopes = sorted( base[2] )

    #remove base from list
    asteroids.remove( base )

    count = 0
    print(base[0])
    removed_asteroids = []
    while count < len(asteroids):
        for angle in slopes:
            currTarget = None
            for asteroid in asteroids:
                if asteroid[0] in removed_asteroids:
                    continue
                currAngle = get_angle(base[0], asteroid[0])
                if currAngle == angle:
                    if not currTarget:
                        currTarget = asteroid[0]
                    else:
                        oldDist = get_dist(base[0], currTarget)
                        newDist = get_dist(base[0], asteroid[0])
                        if newDist < oldDist:
                            currTarget = asteroid[0]

            if currTarget:
                count += 1
                print(currTarget, angle)

                removed_asteroids.append(currTarget)
                if count == 200:
                    print( currTarget )
                    return


main()