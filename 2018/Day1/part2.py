import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    freq = 0
    freq_hit = []
    freq_hit.append(0)

    while True:
        for line in lines:
            freq += int(line)
            #print(freq)
            #print(freq_hit)
            if freq in freq_hit:
                print( "Repeated frequency: ", freq )
                return
            freq_hit.append(freq)

main()