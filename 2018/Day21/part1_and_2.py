import sys

def program():
    r0 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    # ip = 0
    r5 = 0

    results = []

    r3 = r1 | 0x10000 # <- ip = 5 goes here
    r1 = 0x677465
    while True:
        r2 = r3 & 0xFF  # <- ip = 7 goes here
        r1 += r2
        r1 = r1 & 0xFFFFFF
        r1 = r1 * 0x1016B
        r1 = r1 & 0xFFFFFF
        
        if 0x100 > r3:
            r2 = 1
            # Part 1
            #print(r1) #testing
            #return #testing

            # Part 2
            # print([r1,r2])
            if not r1 in results:
                results.append(r1)
            else:
                print(results.pop())
                return

            if r1 == r0:
                break
            else:
                r2 = 0
                r3 = r1 | 0x10000
                r1 = 0x677465
                continue
        else:
            r2 = 0
            while True:
                r5 = r2 + 1
                r5 = r5 * 0x100

                if r5 > r3:
                    r3 = r2
                    break
                else:
                    r2 = r2 + 1
                    continue

program()