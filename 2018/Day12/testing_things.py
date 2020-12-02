import sys
def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    lines.sort()

    for x in lines:
        print(x.strip())


main()