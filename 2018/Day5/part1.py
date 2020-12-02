import sys

def main():
    file = open(sys.argv[1], 'r')
    line = file.readline()

    # print(line)
    # print(len(line)-1)
    while True:
        removed_something = False
        for x in range(len(line)-1):
            if (line[x].upper() == line[x+1] and line[x] == line[x+1].lower()) or (line[x].lower() == line[x+1] and line[x] == line[x+1].upper()):
                # print(line[x],line[x+1])
                line = line[:x] + line[x+2:]
                removed_something = True
                break
        
        # print(line)
        if not removed_something:
            print(len(line)-1)
            return

main()