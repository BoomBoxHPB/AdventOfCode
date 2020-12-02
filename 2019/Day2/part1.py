import sys

def main():
    file = open(sys.argv[1], 'r')
    intcodes = file.readline().split(',')
    intcodes = [int(x) for x in intcodes]

    intcodes[1] = 12
    intcodes[2] = 2

    index = 0
    while True:
        if intcodes[index] == 1:
            a = intcodes[intcodes[index+1]]
            b = intcodes[intcodes[index+2]]
            intcodes[intcodes[index+3]] = a + b

        elif intcodes[index] == 2:
            a = intcodes[intcodes[index+1]]
            b = intcodes[intcodes[index+2]]
            intcodes[intcodes[index+3]] = a * b

        elif intcodes[index] == 99:
            break
        
        index = index + 4

    print(intcodes[0])    

main()