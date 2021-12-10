def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    binInput = [l for l in file.readlines()]
    binSize = len(binInput[0].strip())

    oneMap = [0] * binSize
    zeroMap = [0] * binSize

    for bin in binInput:
        for i in range(0, len(bin.strip())):
            if bin[i] == '0':
                zeroMap[i] += 1
            else:
                oneMap[i] += 1

    # print(oneMap, zeroMap)
    gamma = []
    epsilon = []
    for i in range(0, len(bin.strip())):
        if zeroMap[i] > oneMap[i]:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    print(gamma, epsilon)
    gamma = int(''.join(gamma),2)
    epsilon = int(''.join(epsilon),2)
    print(gamma, epsilon)
    print(gamma * epsilon)

    oxygen = ''
    for i in range(0, binSize):
        zeroCount = 0
        oneCount = 0
        lastBin = ''

        for bin in binInput:
            if bin.startswith(oxygen):
                lastBin = bin
                if bin[i] == '0':
                    zeroCount += 1
                else:
                    oneCount += 1

        if zeroCount + oneCount == 1:
            oxygen = lastBin
            break

        if zeroCount > oneCount:
            oxygen += '0'
        else:
            oxygen += '1'

    co2Scrubber = ''
    for i in range(0, binSize):
        zeroCount = 0
        oneCount = 0
        lastBin = ''

        for bin in binInput:
            if bin.startswith(co2Scrubber):
                lastBin = bin
                if bin[i] == '0':
                    zeroCount += 1
                else:
                    oneCount += 1

        if zeroCount + oneCount == 1:
            co2Scrubber = lastBin
            break

        if zeroCount <= oneCount:
            co2Scrubber += '0'
        else:
            co2Scrubber += '1'
        # print(co2Scrubber)

    print(oxygen, co2Scrubber)
    oxygen = int(oxygen,2)
    co2Scrubber = int(co2Scrubber,2)
    print(oxygen, co2Scrubber)
    print(oxygen * co2Scrubber)



main()
