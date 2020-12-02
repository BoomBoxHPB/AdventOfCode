import sys

ra = 0
rb = 0
rc = 1#0
rd = 0

def get_reg(r):
    global ra
    global rb
    global rc
    global rd

    if r == 'a':
        return ra
    if r == 'b':
        return rb
    if r == 'c':
        return rc
    if r == 'd':
        return rd

def set_reg(r,v):
    global ra
    global rb
    global rc
    global rd

    if r == 'a':
        ra = v
    if r == 'b':
        rb = v
    if r == 'c':
        rc = v
    if r == 'd':
        rd = v

def is_reg(r):
    if r == 'a':
        return True
    if r == 'b':
        return True
    if r == 'c':
        return True
    if r == 'd':
        return True
    return False

def main():
    global ra
    global rb
    global rc
    global rd
    insts = open(sys.argv[1], 'r').readlines()

    for i in range(len(insts)):
        insts[i] = insts[i].strip().split(' ')

    i = 0

    while i < len(insts):
        cur_i = insts[i]
        # print(i)
        if cur_i[0] == 'inc':
            v = get_reg(cur_i[1])
            set_reg(cur_i[1], v + 1)
            i += 1
        elif cur_i[0] == 'dec':
            v = get_reg(cur_i[1])
            set_reg(cur_i[1], v - 1)
            i += 1
        elif cur_i[0] == 'cpy':
            v = 0
            if is_reg(cur_i[1]):
                v = get_reg(cur_i[1])
            else:
                v = int(cur_i[1])
            set_reg(cur_i[2],v)
            i += 1
        elif cur_i[0] == 'jnz':
            v = 0
            if is_reg(cur_i[1]):
                v = get_reg(cur_i[1])
            else:
                v = int(cur_i[1])
            if v != 0:
                i += int(cur_i[2])
            else:
                i += 1
        else:
            print("bad inst: ", cur_i[0])
            return
    
    print("a: ", ra)
    print("b: ", rb)
    print("c: ", rc)
    print("d: ", rd)


main()