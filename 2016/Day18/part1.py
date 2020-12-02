import sys

rows = []
rows.append(list(open(sys.argv[1], 'r').readline()))
print(rows[0])
print(len(rows[0]))
# for i in range(0,39):
for i in range(0,400000-1):
    rows.append('')
    if rows[i][1] == '^':
        rows[i+1] += '^'
    else:
        rows[i+1] += '.'
    
    for j in range(1,len(rows[0])-1):
        if rows[i][j-1] != rows[i][j+1]:
            rows[i+1] += '^'
        else:
            rows[i+1] += '.'
    
    if rows[i][len(rows[0])-2] == '^':
        rows[i+1] += '^'
    else:
        rows[i+1] += '.'

cnt = 0
for row in rows:
    cnt += row.count('.')

print(cnt)