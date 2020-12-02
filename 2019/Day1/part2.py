import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    total = 0

    for line in lines:
        mass = int(line)
        while( mass > 0 ):
            mass = ( mass // 3 ) - 2
            total += max( mass, 0 )

    print( total )

main()