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
    opcodes = {
        "addr": addr,
        "addi": addi,
        "mulr": mulr,
        "muli": muli,
        "banr": banr,
        "bani": bani,
        "borr": borr,
        "bori": bori,
        "setr": setr,
        "seti": seti,
        "gtir": gtir,
        "gtri": gtri,
        "gtrr": gtrr,
        "eqir": eqir,
        "eqri": eqri,
        "eqrr": eqrr
    }

    file = open(sys.argv[1], 'r')
    ip_reg = int(file.readline().split()[1])
    ip_value = 0
    program = []
    regs = [0 for x in range(6)]
    regs[0] = 1

    for line in file:
        parts = line.split()
        parts[1] = int(parts[1])
        parts[2] = int(parts[2])
        parts[3] = int(parts[3])
        program.append(parts)

    while True:
        regs[ip_reg] = ip_value

        if ip_value <= 5:
            print(regs, ip_value)

        curr_inst = program[ip_value]
        regs = opcodes[curr_inst[0]](curr_inst, regs)
        # print(opcodes[curr_inst[0]])

        ip_value = regs[ip_reg] + 1

        if ip_value >= len(program):
            print(regs, ip_value)
            return


main()