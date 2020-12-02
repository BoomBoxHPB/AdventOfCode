import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    freq = 0

    for line in lines:
        freq += int(line)

    print( freq )

main()