import sys

def main():
    lines = open(sys.argv[1], 'r').readlines()
    total = 0

    for line in lines:
        nums = line.split()
        max = int(nums[0])
        min = max

        for n in range(1,len(nums)):
            ni = int(nums[n])
            if ni > max:
                max = ni
            elif ni < min:
                min = ni
        
        total += (max - min)
    
    print(total)

main()