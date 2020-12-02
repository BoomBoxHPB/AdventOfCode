import sys

def main():
    lines = open(sys.argv[1], 'r').readlines()
    total = 0

    for line in lines:
        nums = line.split()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                ni = int(nums[i])
                nj = int(nums[j])

                if ni % nj == 0:
                    total += ni / nj
                # Not sure how to escape both loops...

    print(total)

main()