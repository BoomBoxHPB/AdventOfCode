#!/usr/bin/env python3
import sys
# import re
import copy
import utils

def validate(preamble, num):
    for i in range(len(preamble)-1):
        d1 = preamble[i]
        for d2 in preamble[i+1:]:
            if d1 != d2 and d1 + d2 == num:
                return True

    return False

def findRange(list, num):
    max_len = len(list)
    for i in range(max_len - 1):
        for j in range(i + 1, max_len):
            r = list[i:j]
            total = sum(r)
            if total == num:
                return min(r) + max(r)
            if total > num:
                break

    return 0

def main():
    data = [int(line) for line in utils.read_lines()]

    i = 25
    # i = 5 # test case

    while True:
        if not validate(data[i-25:i], data[i]):
            print('Part1 {}'.format(data[i]))

            r = findRange(data, data[i])
            print('Part2 {}'.format(r))
            break
        i += 1



main()
