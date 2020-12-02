import sys

class Moon:
    def __init__(self, startPosition):
        self.position = startPosition[:]
        self.velocity = [0,0,0]

    def __repr__(self):
        return "pos={}, vel={}\n".format(self.position, self.velocity)

    def ApplyGravity(self, otherMoon):
        # print(self.velocity)
        for i in range(3):
            if self.position[i] > otherMoon.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < otherMoon.position[i]:
                self.velocity[i] += 1

    def IncrementTime(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def GetEnergy(self):
        pot = sum([abs(p) for p in self.position])
        ken = sum([abs(v) for v in self.velocity])
        return pot * ken

def main():
    f = open(input("Filename: "), 'r')
    coordinates = [line.split(',') for line in f.readlines()]
    coordinates = [[int(s.strip('<> xyz=\n')) for s in coor] for coor in coordinates]
    
    print(coordinates)

    Moons = [Moon(coor) for coor in coordinates]
    timeSteps = 0

    print(Moons)
    while True:
        for moon1 in Moons:
            for moon2 in Moons:
                if moon1 is not moon2:
                    moon1.ApplyGravity(moon2)

        for moon in Moons:
            moon.IncrementTime()

        timeSteps += 1
        # print("After {} steps:".format(timeSteps))
        # print(Moons)
        
        if timeSteps == 1000:
            break

    totalEnergy = sum([moon.GetEnergy() for moon in Moons])
    print("Total energy after {} steps in {}".format(timeSteps, totalEnergy))


main()