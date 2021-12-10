#!/usr/bin/env python3
import sys
import utils

class Seat:
    def __init__(self, line):
        reversed = line[::-1]
        self.uid = 0

        n = 0
        for c in reversed:
            if c == 'B' or c == 'R':
                self.uid += (1 << n)
            n += 1

        # print('{}: UID = {}'.format(line, self.uid))



def main():
    seats = [Seat(line) for line in utils.read_lines()]

    max_uid = 0
    for seat in seats:
        max_uid = max(max_uid, seat.uid)
    print("Part1: {}".format(max_uid))

    max_row_id = Seat('BBBBBBBRRR').uid

    seats_exist = []
    for i in range(max_row_id):
        found = False
        for seat in seats:
            # print(seat.uid)
            if seat.uid == i:
                found = True
                break

        seats_exist.append(found)

    # print(seats_exist)

    for i in range(8, max_row_id):
        if seats_exist[i-1] and seats_exist[i + 1] and not seats_exist[i]:
            print('Part2: {}'.format(i))
            break

main()
