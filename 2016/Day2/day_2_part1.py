import sys

def main():
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    pos = [0,0]
    file = open(sys.argv[1], 'r')

    for raw in file:
        for i in raw:
            if i == 'U':
                pos[0] -= 1
            elif i == 'D':
                pos[0] += 1
            elif i == 'L':
                pos[1] -= 1
            elif i == 'R':
                pos[1] += 1
            # Get back in bounds
            if pos[0] < 0: pos[0] = 0
            elif pos[0] > 2: pos[0] = 2
            elif pos[1] < 0: pos[1] = 0
            elif pos[1] > 2: pos[1] = 2
        
        print( "Key: ", keypad[pos[0]][pos[1]] )
main()