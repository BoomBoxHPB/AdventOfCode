#!/usr/bin/env python3.6
import sys

def main():
    f = open(input("Filename: "), 'r')
    values = [int(line) for line in f.readlines()]
    # print(values)

    # We get duplicates since we'll get both (val1,val2) and (val2,val1)
    # Can work to avoid this, but it's not too bad and gets us the output we need.
    for val1 in values:
        for val2 in values:
            if val1 + val2 == 2020:
                print("{} and {} give us {}".format(val1, val2, val1 * val2))

    for val1 in values:
        for val2 in values:
            for val3 in values:
                if val1 + val2 + val3 == 2020:
                    print("{}, {}, and {} give us {}".format(val1, val2, val3, val1 * val2 * val3))

main()
