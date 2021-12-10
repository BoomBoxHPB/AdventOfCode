import sys

def read_lines():
    f = open(input("Filename: "), 'r')
    return [line.strip() for line in f.readlines()]
