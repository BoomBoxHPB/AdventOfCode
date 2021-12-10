#!/usr/bin/env python3
import sys
# import re
import copy
import utils

def parseCode(line):
    parts = line.split()
    parts[1] = int(parts[1])
    # print(parts)
    return parts

def main():
    codes = [parseCode(line) for line in utils.read_lines()]

    accumulator = 0
    pc = 0
    visited_codes = []

    while pc not in visited_codes:
        visited_codes.append(pc)
        code = codes[pc]
        # print(code)

        if code[0] == 'nop':
            pc += 1
        elif code[0] == 'acc':
            accumulator += code[1]
            pc += 1
        elif code[0] == 'jmp':
            pc += code[1]

    print('Part1: {}'.format(accumulator))

    for i in range(len(codes)):
        new_codes = copy.deepcopy(codes)
        flipped_code = new_codes[i]
        if flipped_code[0] == 'nop':
            flipped_code[0] = 'jmp'
        elif flipped_code[0] == 'jmp':
            flipped_code[0] = 'nop'

        accumulator = 0
        pc = 0
        visited_codes = []

        while pc not in visited_codes and pc != len(new_codes):
            visited_codes.append(pc)
            code = new_codes[pc]
            # print(code)

            if code[0] == 'nop':
                pc += 1
            elif code[0] == 'acc':
                accumulator += code[1]
                pc += 1
            elif code[0] == 'jmp':
                pc += code[1]

        if pc == len(new_codes):
            print('Part2 {}'.format(accumulator))
            break


main()
