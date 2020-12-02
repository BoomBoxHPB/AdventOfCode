import sys

steps = []

for i in list(open(sys.argv[1], 'r').readline()):
    steps.append(ord(i))

steps += [17, 31, 73, 47, 23]

nums = list(range(256))
skip_num = 0
curr_pos = 0

for rnd in range(64):
    for leng in steps:
        temp_end = curr_pos+leng
        temp_list = nums[curr_pos:temp_end]
        if temp_end > 256:
            temp_list += nums[0:temp_end%256]

        for i in range(leng):
            orig_i = ( i + curr_pos ) % 256
            nums[orig_i] = temp_list[len(temp_list) - i - 1]
        # print(temp_list)

        curr_pos += leng + skip_num
        curr_pos %= 256
        skip_num += 1

sparse = []

for i in range(0,256,16):
    temp = 0
    for j in range(i,i+16):
        temp ^= nums[j]
    
    sparse.append(temp)

hex_out = ''

for i in sparse:
    hex_out += "%0.2X" % i

print(hex_out)