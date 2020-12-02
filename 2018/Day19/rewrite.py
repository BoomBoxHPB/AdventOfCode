import sys

def main():
    r = [0 for x in range(6)]
    r[0] = 1

    r[5] += 2
    r[5] *= r[5]
    r[5] *= 19
    r[5] *= 11
    r[4] += 5
    r[4] *= 22
    r[4] += 9
    r[5] += r[4]

    if r[0] != 0:
        r[4] = 27
        r[4] *= 28
        r[4] += 29
        r[4] *= 30
        r[4] *= 14
        r[4] *= 32
        r[5] += r[4]
        r[0] = 0
    
    r[1] = 1
    while True:
        r[3] = 1
        while True:
            r[4] = r[1] * r[3]
            if r[4] == r[5]:
                r[4] = 1
            else:
                r[4] = 0
            if r[4] != 0:
                r[0] += r[1]
            r[3] += 1
            if r[3] > r[5]:
                r[4] = 1
            else:
                r[4] = 0
            if r[4] == 0:
                continue
            r[1] += 1
            if r[1] > r[5]:
                r[4] = 1
            else:
                r[4] = 0
            if r[4] == 0:
                break
            else:
                print(r)
                return

def main_opt1():
    r = [0 for x in range(6)]
    r[0] = 1

    r[5] += 2
    r[5] *= r[5]
    r[5] *= 19
    r[5] *= 11
    r[4] += 5
    r[4] *= 22
    r[4] += 9
    r[5] += r[4]

    if r[0] != 0:
        r[4] = 27
        r[4] *= 28
        r[4] += 29
        r[4] *= 30
        r[4] *= 14
        r[4] *= 32
        r[5] += r[4]
        r[0] = 0
    
    r[1] = 1
    while True:
        r[3] = 1
        while True:
            r[4] = r[1] * r[3]
            if r[4] == r[5]:
                r[4] = 1
                r[0] += r[1]
                r[1] += 1
                break
            else:
                r[4] = 0
                
            r[3] += 1
            if r[3] > r[5]:
                r[4] = 1
            else:
                r[4] = 0
                continue
            r[1] += 1
            if r[1] > r[5]:
                r[4] = 1
                print(r)
                return
            else:
                r[4] = 0
                break

def main_opt2():
    r = [0 for x in range(6)]
    r[0] = 1

    r[5] += 2
    r[5] *= r[5]
    r[5] *= 19
    r[5] *= 11
    r[4] += 5
    r[4] *= 22
    r[4] += 9
    r[5] += r[4]

    if r[0] != 0:
        r[4] = 27
        r[4] *= 28
        r[4] += 29
        r[4] *= 30
        r[4] *= 14
        r[4] *= 32
        r[5] += r[4]
        r[0] = 0
    
    for x in range(1,r[5] + 1):
        if r[5] % x == 0:
            r[0] += x
            print(x)
    
    print(r)

main_opt2()