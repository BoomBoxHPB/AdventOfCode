import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    grid = [[False for x in range(6)] for y in range(50)]
    count = 0
        
    for L in lines:
        words = L.split()
        
        if( words[0] == 'rect' ):
            x_y = words[1].split('x')
            
            for i in range(int(x_y[0])):
                for j in range(int(x_y[1])):
                    grid[i][j] = True
            
        elif( words[0] == 'rotate' ):
            shift = int(words[4])
            pos = int(words[2].split('=')[1])
            
            if( words[1] == 'row' ):
                orig = []
                for i in range(50):
                    orig.append(grid[i][pos])
                
                for i in range(50):
                    grid[(i+shift)%50][pos] = orig[i]
                
            elif( words[1] == 'column' ):
                orig = grid[pos][:]
                for i in range(6):
                    grid[pos][(i+shift)%6] = orig[i]
    
    for i in range(50):
        for j in range(6):
            if grid[i][j]:
                count += 1
    
    print( count )
    
    for j in range(6):
        row = []
        for i in range(50):
            if(grid[i][j]):
                row.append('#')
            else:
                row.append('.')
        row_str = ''.join(row)
        print(row_str)
    
main()