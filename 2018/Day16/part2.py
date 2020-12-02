import sys

def addr(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] + out_regs[inst[2]]
    return out_regs

def addi(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] + inst[2]
    return out_regs

def mulr(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] * out_regs[inst[2]]
    return out_regs

def muli(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] * inst[2]
    return out_regs

def banr(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] & out_regs[inst[2]]
    return out_regs

def bani(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] & inst[2]
    return out_regs

def borr(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] | out_regs[inst[2]]
    return out_regs

def bori(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]] | inst[2]
    return out_regs

def setr(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = out_regs[inst[1]]
    return out_regs

def seti(inst, in_regs):
    out_regs = list(in_regs)
    out_regs[inst[3]] = inst[1]
    return out_regs

def gtir(inst, in_regs):
    out_regs = list(in_regs)
    if inst[1] > out_regs[inst[2]]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def gtri(inst, in_regs):
    out_regs = list(in_regs)
    if out_regs[inst[1]] > inst[2]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def gtrr(inst, in_regs):
    out_regs = list(in_regs)
    if out_regs[inst[1]] > out_regs[inst[2]]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def eqir(inst, in_regs):
    out_regs = list(in_regs)
    if inst[1] == out_regs[inst[2]]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def eqri(inst, in_regs):
    out_regs = list(in_regs)
    if out_regs[inst[1]] == inst[2]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def eqrr(inst, in_regs):
    out_regs = list(in_regs)
    if out_regs[inst[1]] == out_regs[inst[2]]:
        out_regs[inst[3]] = 1
    else:
        out_regs[inst[3]] = 0
    return out_regs

def main():
    opcodes = [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr
    ]
    real_ops = [0 for x in range(len(opcodes))]
    file = open(sys.argv[1], 'r')
    
    while True:
        b_parts = file.readline().split(':')
        # print(b_parts)
        if b_parts[0] != "Before":
            break
        
        b_regs = list(map(int, b_parts[1].strip(' []\n').split(',')))
        
        # print(b_regs)

        inst = list(map(int, file.readline().strip().split()))

        # print(inst)

        a_regs = list(map(int, file.readline().split(':')[1].strip(' []\n').split(',')))

        # print(a_regs)

        # Read blank line
        file.readline()

        potential = []

        for op in opcodes:
            if a_regs == op(inst, b_regs):
                potential.append(op)

        # lazy accounting for collisions
        if len(potential) == 1 and real_ops[inst[0]] == 0:
            # print(inst, potential, file.tell())
            # if real_ops[inst[0]] != 0:
            #     print("Conflict! ", real_ops[inst[0]], potential[0] )
            #     print(b_regs, inst, a_regs)
            real_ops[inst[0]] = potential[0]
            opcodes.remove(potential[0])
            file.seek(0,0) # go back to the beginning of the list to see if we can learn more
    
    # print(real_ops)    
    # print(opcodes)

    file.readline() # another blank line

    regs = [0, 0, 0, 0]
    while True:
        inst = list(map(int, file.readline().strip().split()))
        if len(inst) == 0:
            break
        # print(inst)
        # print(real_ops[inst[0]])
        regs = real_ops[inst[0]](inst, regs)
    
    print(regs)
main()