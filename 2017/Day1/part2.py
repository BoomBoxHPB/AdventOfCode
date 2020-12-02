import sys

def main():
    file = open(sys.argv[1], 'r')
    captcha_str = file.readline()
    captcha_nums = []
    total = 0

    for ch in captcha_str:
        captcha_nums.append(int(ch))

    nums_len = len(captcha_nums)
    
    def other_i(i):
        i += ( nums_len / 2 )
        i %= nums_len
        return int(i)

    for num in range(len(captcha_nums)):
        if captcha_nums[num] == captcha_nums[other_i(num)]:
            total += captcha_nums[num]
    
    print( total )

main()