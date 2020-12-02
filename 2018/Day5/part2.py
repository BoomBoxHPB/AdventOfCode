import sys
import string

def main():
    file = open(sys.argv[1], 'r')
    line = file.readline()
    string_lens = []

    # print(line)
    # print(len(line)-1)
    for ch in string.ascii_lowercase:
        # line_copy = line[:]
        # while True:
        #     removed_something = False
            
        #     for x in range(len(line_copy)-1):
        #         if ch == line_copy[x].lower():
        #             # print(line[x],line[x+1])
        #             line_copy = line_copy[:x] + line_copy[x+1:]
        #             removed_something = True
        #             break
            
        #     if not removed_something:
        #         break;
        line_copy = []
        line_copy[:] = [x for x in line if x.lower() != ch]
        print("Removed ", ch)

        while True:
            removed_something = False
            for x in range(len(line_copy)-1):
                if (line_copy[x].upper() == line_copy[x+1] and line_copy[x] == line_copy[x+1].lower()) or (line_copy[x].lower() == line_copy[x+1] and line_copy[x] == line_copy[x+1].upper()):
                    # print(line_copy[x],line_copy[x+1])
                    line_copy = line_copy[:x] + line_copy[x+2:]
                    removed_something = True
                    break
            if not removed_something:
                break;

        print("Collapsed string")
        # print(line_copy)
        # print(ch, len(line_copy))
        string_lens.append(len(line_copy))
    
    print(min(string_lens)-1)

main()