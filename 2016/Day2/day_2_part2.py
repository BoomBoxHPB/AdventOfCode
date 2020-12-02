import sys

def main():
    keypad = [[  0,  0,'1',  0,  0],
              [  0,'2','3','4',  0],
              ['5','6','7','8','9'],
              [  0,'A','B','C',  0],
              [  0,  0,'D',  0,  0]]
    mins = [2,1,0,1,2]
    maxs = [2,3,4,3,2]
    pos = [2,0]
    file = open(sys.argv[1], 'r')

    for raw in file:
        for i in raw:
            if i == 'U':
                pos[0] -= 1
                pos[0] = min(max(pos[0],mins[pos[1]]),maxs[pos[1]])
            elif i == 'D':
                pos[0] += 1
                pos[0] = min(max(pos[0],mins[pos[1]]),maxs[pos[1]])
            elif i == 'L':
                pos[1] -= 1
                pos[1] = min(max(pos[1],mins[pos[0]]),maxs[pos[0]])
            elif i == 'R':
                pos[1] += 1
                pos[1] = min(max(pos[1],mins[pos[0]]),maxs[pos[0]])
        
        print( "Key: ", keypad[pos[0]][pos[1]] )
main()