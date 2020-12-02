import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    total = 0

    for line in lines:
        total += ( int(line) // 3 ) - 2

    print( total )

main()