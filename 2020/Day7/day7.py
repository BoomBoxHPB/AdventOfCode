#!/usr/bin/env python3
import sys
import re
import utils

class Rules:
    def __init__(self):
        self.bags = {}

    def AddRule(self, line):
        s = re.split(' bags contain |, ', line)
        contents = {}

        if not s[1].startswith('no'):
            for entry in s[1:]:
                temp = entry.split()
                contents['{} {}'.format(temp[1], temp[2])] = int(temp[0])

        self.bags[s[0]] = contents
        # print(s[0], ' ', self.bags[s[0]])

    def GetBags(self):
        return self.bags.keys()

    def GetContents(self, bag):
        return self.bags[bag].keys()

    def GetContents2(self, bag):
        return self.bags[bag]


def main():
    lines = utils.read_lines()

    rules = Rules()
    for line in lines:
        rules.AddRule(line)

    holders = set()
    def RecursiveFind(bag, key):
        add = False
        if bag in holders:
            return True

        contents = rules.GetContents(bag)
        if key in contents:
            add = True
        else:
            for x in rules.GetContents(bag):
                # print(x)
                if x in holders:
                    add = True
                elif RecursiveFind(x, key):
                    add = True

        if add:
            holders.add(bag)

        return add

    mine = 'shiny gold'
    for bag in rules.GetBags():
        RecursiveFind(bag, mine)
    print(holders)
    print('Part1: {}'.format(len(holders)))


    # Part 2
    def GetCount(bag):
        total = 0
        contents = rules.GetContents2(bag)
        for x in rules.GetContents2(bag):
            count = contents[x]
            total += count * (1 + GetCount(x))

        return total

    print(GetCount(mine))

main()
