import sys

lines = open(sys.argv[1], 'r').readlines()
lists = []
cnt = 0

for line in lines:
    lists.append(line.split())
    lists[cnt][1] = lists[cnt][1].strip('()')
    if len(lists[cnt]) > 2:
        del lists[cnt][2]
    for i in range(2,len(lists[cnt])):
        lists[cnt][i] = lists[cnt][i].strip(',')

    cnt += 1

# print(lists)

# Gonna brute force this...
for line in lists:
    found = False

    for line2 in lists:
        if not found and line != line2:
            # print( line2 )
            if line[0] in line2:
                found = True
                continue
    
    if not found:
        print(line[0])
        break
