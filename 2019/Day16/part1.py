import sys

def GetMultiplier(iteration, index):
    pattern = [0,1,0,-1]
    realIndex = ( index + 1 ) // ( iteration + 1 )
    realIndex %= len(pattern)
    # print(iteration, index, pattern[realIndex])
    return pattern[realIndex]

def main():
    f = open(input("Filename: "), 'r')
    pattern = [int(i) for i in f.readline().strip()]

    print(pattern)
    
    for phase in range(100):
        newPattern = []

        for i in range(len(pattern)):
            total = 0
            for j in range(len(pattern)):
                total += pattern[j] * GetMultiplier(i, j)
            
            total = abs(total) % 10
            newPattern.append(total)
        
        # print(newPattern)
        pattern = newPattern[:]

    print(pattern[0:8])

main()