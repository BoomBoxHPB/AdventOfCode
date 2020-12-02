import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    
    # grid[y][x]
    grid = [0 for x in range(len(lines))]
    carts = []

    y = 0
    for line in lines:
        grid[y] = [' ' for x in range(len(line)-1)]

        for x in range(len(line)-1):
            if line[x] == '^' or line[x] == 'v':
                carts.append([line[x],[x,y],'l',False])
                grid[y][x] = '|'
            elif line[x] == '<' or line[x] == '>':
                carts.append([line[x],[x,y],'l',False])
                grid[y][x] = '-'
            else:
                grid[y][x] = line[x]
        
        y += 1
    
    # for line in grid:
    #     print(line)

    # print(carts)

    collision = False
    
    # while collision: 
    while not collision:
        to_remove = []
        carts.sort(key=lambda x: x[1][1]) # sort by y
        carts.sort(key=lambda x: x[1][0]) # sort by x (preserves y sorting)
        # print(carts)
        for cart in carts:
            if cart[3] == True:
                continue
            ch = cart[0]
            loc = cart[1] # x,y
            if ch == '^':
                # y - 1
                loc[1] -= 1
                if grid[loc[1]][loc[0]] == '/':
                    cart[0] = '>'
                elif grid[loc[1]][loc[0]] == '\\':
                    cart[0] = '<'
                elif grid[loc[1]][loc[0]] == '+':
                    if cart[2] == 'l':
                        cart[0] = '<'
                        cart[2] = 's'
                    elif cart[2] == 's':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[0] = '>'
                        cart[2] = 'l'
                
            elif ch == '>':
                # x + 1
                loc[0] += 1
                if grid[loc[1]][loc[0]] == '/':
                    cart[0] = '^'
                elif grid[loc[1]][loc[0]] == '\\':
                    cart[0] = 'v'
                elif grid[loc[1]][loc[0]] == '+':
                    if cart[2] == 'l':
                        cart[0] = '^'
                        cart[2] = 's'
                    elif cart[2] == 's':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[0] = 'v'
                        cart[2] = 'l'

            elif ch == 'v':
                # y + 1
                loc[1] += 1
                if grid[loc[1]][loc[0]] == '/':
                    cart[0] = '<'
                elif grid[loc[1]][loc[0]] == '\\':
                    cart[0] = '>'
                elif grid[loc[1]][loc[0]] == '+':
                    if cart[2] == 'l':
                        cart[0] = '>'
                        cart[2] = 's'
                    elif cart[2] == 's':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[0] = '<'
                        cart[2] = 'l'

            elif ch == '<':
                # x - 1
                loc[0] -= 1
                if grid[loc[1]][loc[0]] == '/':
                    cart[0] = 'v'
                elif grid[loc[1]][loc[0]] == '\\':
                    cart[0] = '^'
                elif grid[loc[1]][loc[0]] == '+':
                    if cart[2] == 'l':
                        cart[0] = 'v'
                        cart[2] = 's'
                    elif cart[2] == 's':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[0] = '^'
                        cart[2] = 'l'

            # check for collisions
            for cart2 in carts:
                if cart != cart2 and cart2[3] == False:
                    loc2 = cart2[1]
                    # print( loc, loc2)
                    if loc[0] == loc2[0] and loc[1] == loc2[1]:
                        cart[3] = True
                        to_remove.append(cart)
                        cart2[3] = True
                        to_remove.append(cart2)
                        break
            
        for c in to_remove:
            carts.remove(c)  

        if len(carts) <= 1:
            collision = True
            break

        # print(carts)
    print(carts[0][1])
main()