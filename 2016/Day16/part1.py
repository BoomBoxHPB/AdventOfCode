start = 10111011111001111
disk_size = 35651584#272

data = str(start)

# print(data)

while len(data) < disk_size:
    data += '0'
    for i in range(len(data)-2, -1, -1):
        if data[i] == '0':
            data += '1'
        elif data[i] == '1':
            data += '0'
    # print(len(data))
    # print(data)

chksum = data[0:disk_size]

while len(chksum) % 2 == 0:
    data = chksum
    chksum = ''

    for i in range(0,len(data),2):
        if data[i] == data[i+1]:
            chksum += '1'
        else:
            chksum += '0'
print(chksum)
