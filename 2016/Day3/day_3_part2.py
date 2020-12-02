import sys

def main():
    file = open(sys.argv[1], 'r')
    row_count = 0
    good_count = 0
    
    for raw in file:
        entries = raw.split()
        if row_count == 0:
            a1 = int(entries[0])
            a2 = int(entries[1])
            a3 = int(entries[2])
            row_count += 1
        elif row_count == 1:
            b1 = int(entries[0])
            b2 = int(entries[1])
            b3 = int(entries[2])
            row_count += 1
        elif row_count == 2:
            c1 = int(entries[0])
            c2 = int(entries[1])
            c3 = int(entries[2])
            if a1+b1>c1:
                if b1+c1>a1:
                    if a1+c1>b1:
                        good_count += 1
            if a2+b2>c2:
                if b2+c2>a2:
                    if a2+c2>b2:
                        good_count += 1
            if a3+b3>c3:
                if b3+c3>a3:
                    if a3+c3>b3:
                        good_count += 1
            row_count = 0
    
    print("Good triangles: ", good_count)
main()