#!/usr/bin/env python3
import sys
import utils

class Passport:
    def __init__(self, line):
        self.fields = [x.split(':') for x in line.split()]
        # print(self.fields)

    def IsValid1(self):
        required_fields = [
            'byr', 'iyr', 'eyr',
            'hgt', 'hcl', 'ecl',
            'pid'
        ]

        for f in required_fields:
            if not self.findValue(f):
                return False

        return True


    def IsValid2(self):
        # Use the part1 valid check to avoid re-checking later
        if not self.IsValid1():
            return False

        byr = int(self.findValue('byr'))
        if byr < 1920 or byr > 2002:
            print('byr: ', byr)
            return False

        iyr = int(self.findValue('iyr'))
        if iyr < 2010 or iyr > 2020:
            print('iyr: ', iyr)
            return False

        eyr = int(self.findValue('eyr'))
        if eyr < 2020 or eyr > 2030:
            print('eyr: ', eyr)
            return False

        hgt = self.findValue('hgt')
        index = hgt.find('cm')
        # print(index)
        if index != -1:
            if index != 3:
                return False
            num = int(hgt[:index])
            if num < 150 or num > 193:
                return False
        else:
            index = hgt.find('in')
            if index != -1:
                if index != 2:
                    return False
                num = int(hgt[:index])
                if num < 59 or num > 76:
                    return False

        if index == -1:
            return False

        hcl = self.findValue('hcl')
        if len(hcl) != 7 or hcl[0] != '#':
            return False
        for c in hcl[1:]:
            vals = '0123456789abcdef'
            if c not in vals:
                return False

        ecl = self.findValue('ecl')
        eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if ecl not in eye_colors:
            print('ecl: ', ecl)
            return False

        pid = self.findValue('pid')
        if len(pid) != 9:
            print('pid: ', pid)
            return False

        return True

    def findValue(self, key):
        for field in self.fields:
            found = False
            for field in self.fields:
                if key == field[0]:
                    return field[1]
            if not found:
                return None



def main():
    lines = utils.read_lines()
    # print(lines)

    squashed_lines = []
    new_line = ''
    for line in lines:
        if line == '':
            squashed_lines.append(new_line.strip())
            new_line = ''
        else:
            new_line += line + ' '
    if new_line != '':
        squashed_lines.append(new_line.strip())
    # print(squashed_lines)

    passports = [Passport(line) for line in squashed_lines]

    count = sum(1 for x in passports if x.IsValid1())
    print("Part1: ", count)

    count = sum(1 for x in passports if x.IsValid2())
    print("Part2: ", count)


main()
