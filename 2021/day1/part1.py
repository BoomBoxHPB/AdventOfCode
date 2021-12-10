import sys

def main():
    filename = input("File name: ")

    file = open(filename, mode='r')
    lastValue = 999999999
    count = 0

    vals = [int(i) for i in file.readlines()]

    for val in vals:
        if val > lastValue:
            count += 1
        lastValue = val

    print(f"Increase count part 1 = {count}")

    lastValue = 999999999
    count = 0

    for i in range(0,len(vals) - 2):
        # print(vals[i:i+3])
        val = sum(vals[i:i+3])
        # print(val)
        if val > lastValue:
            count += 1
        lastValue = val

    print(f"Increase count part 2 = {count}")


main()
