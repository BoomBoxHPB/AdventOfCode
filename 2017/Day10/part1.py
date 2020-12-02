import sys

steps = open(sys.argv[1], 'r').readline().split(',')

nums = list(range(256))
skip_num = 0
curr_pos = 0

for step in steps:
    leng = int(step)
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

print(nums)
print(nums[0] * nums[1])