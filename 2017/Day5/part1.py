import sys

insts_str = open(sys.argv[1], 'r').readlines()
insts = []
for inst in insts_str:
    insts.append(int(inst))

i = 0
cnt = 0

while i < len(insts) and i >= 0:
    old_i = i
    jmp_amnt = insts[i]
    i += jmp_amnt
    #part 2 Only!
    if jmp_amnt >= 3:
        insts[old_i] -= 1
    else:
        insts[old_i] += 1
    cnt += 1
    # print(i)
print(cnt)