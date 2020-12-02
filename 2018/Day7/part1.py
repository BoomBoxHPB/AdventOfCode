import sys
import string

def main():
    file = open(sys.argv[1], 'r')
    inputs = file.readlines()
    seq = []
    result = ""
    for line in inputs:
        pieces = line.split()
        # print(pieces)
        seq.append((pieces[1],pieces[7]))
    
    # print(seq)
    # print(seq[1])
    # print(seq[1][1])

    avail = []
    for x in seq:
        if not (x[0] in avail):
            avail.append(x[0])
        if not (x[1] in avail):
            avail.append(x[1]) 

    avail.sort()
    # print(avail)

    while len(avail) > 0:
        for ch in avail:
            restriction_found = False

            for x in seq:
                if ch == x[1]:
                    restriction_found = True
                    break
            
            if not restriction_found:
                # print("no re found for ", ch)
                result += ch
                while True:
                    something_removed = False
                    for x in seq:
                        if ch == x[0]:
                            # remove x from seq
                            seq.remove(x)
                            something_removed = True
                    if not something_removed:
                        break

                avail.remove(ch)
                # print(seq)
                break

    print(result)

main()