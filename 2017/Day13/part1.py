import sys

def main():
    f = open(sys.argv[1], 'r')
    layers = {}
    end = 0
    curr_layer = -1
    for line in f.readlines():
        parts = line.split(':')
        layers[int(parts[0])] = [int(parts[1].strip()),0,'d']
        end = int(parts[0])
    
    total_severity = 0

    for x in range(end + 1):
        # print(layers)
        curr_layer += 1

        if x in layers and layers[x][1] == 0:
            total_severity += x * layers[x][0]
        
        for layer in layers:
            l = layers[layer]
            if l[1] == l[0]-1:
                l[2] = 'u'
            elif l[1] == 0:
                l[2] = 'd'

            if l[2] == 'd':
                l[1] += 1
            else:
                l[1] -= 1
    
    print(total_severity)


main()