import sys

blocks_str = open(sys.argv[1], 'r').readline().split()
blocks = []
for s in blocks_str:
    blocks.append(int(s))
prev_blocks = []
cnt = 0

while not blocks in prev_blocks:
    prev_blocks.append(blocks[:])
    
    i_max = 0
    for i in range(len(blocks)):
        if blocks[i] > blocks[i_max]:
            i_max = i
    temp = blocks[i_max]
    blocks[i_max] = 0

    # print(temp)
    
    while temp > 0:
        i_max += 1
        if i_max >= len(blocks):
            i_max = 0
        blocks[i_max] += 1
        temp -= 1
        # print(blocks)

    cnt += 1

# print(prev_blocks)
print(cnt)
print(cnt-prev_blocks.index(blocks[:]))