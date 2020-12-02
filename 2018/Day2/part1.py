import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    twos_count = 0
    threes_count = 0

    for line in lines:
        twos_found = False
        threes_found = False
        for ch in line:
            ch_count = line.count(ch)
            if not twos_found and ch_count == 2:
                twos_count += 1
                twos_found = True
            if not threes_found and ch_count == 3:
                threes_count += 1
                threes_found = True

    print( "Checksum = ", twos_count * threes_count )

main()