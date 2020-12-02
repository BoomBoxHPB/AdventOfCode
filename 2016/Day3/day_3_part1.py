import sys

def main():
    file = open(sys.argv[1], 'r')
    good_count = 0
    
    for raw in file:
        entries = raw.split()
        a = int(entries[0])
        b = int(entries[1])
        c = int(entries[2])
        if a+b>c:
            if b+c>a:
                if a+c>b:
                    good_count += 1
    
    print("Good triangles: ", good_count)
main()