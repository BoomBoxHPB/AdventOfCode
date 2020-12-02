import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    discs = []
    time = 0
    
    for d in lines:
        words = d.split()
        positions = int(words[3])
        start_per = list(words[11])
        start = int(''.join(start_per[0:len(start_per)-1]))
        
        discs.append((positions,start))
    
    while True:
        good = True
        t_time = time
        
        for d in discs:
            t_time += 1
            position = (d[1] + t_time) % d[0]
            
            if position != 0:
                good = False
                break
            
        if good:
            break
        else:
            time += 1
    
    print( time )

main()