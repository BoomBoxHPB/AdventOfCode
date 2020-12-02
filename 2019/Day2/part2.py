import sys

def main():
    file = open(sys.argv[1], 'r')
    intcodes = file.readline().split(',')
    original_intcodes = [int(x) for x in intcodes]

    for noun in range(100):
        for verb in range(100):
            index = 0
            intcodes = original_intcodes[:]
            intcodes[1] = noun
            intcodes[2] = verb

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
            
            if intcodes[0] == 19690720:
                print("noun = {}, verb = {}".format(noun, verb))
                print("total = {}".format(noun*100 + verb))
                exit

    # print(intcodes[0])    

main()