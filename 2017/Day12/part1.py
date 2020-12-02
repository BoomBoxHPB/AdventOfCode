import sys

def search_group(grps, z_grp, cur):
    items = grps[cur]
    # print(items)
    for i in items:
        if i not in z_grp:
            z_grp.append(i)
            search_group(grps, z_grp, i)


groups = {}

for line in open(sys.argv[1], 'r').readlines():
    pieces = line.split()
    grp = []
    for i in range(2,len(pieces)):
        grp.append(pieces[i].strip(','))
    groups[pieces[0]] = grp

# print(groups)

zero_group = ['0']

search_group(groups, zero_group, '0')

print(zero_group)
print(len(zero_group))