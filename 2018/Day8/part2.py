import sys
from collections import deque

def node(children_cnt, metadata_cnt, list_of_things):  
    metadata_sum = 0

    if children_cnt == 0:
        for x in range(metadata_cnt):
            metadata_sum += int(list_of_things.popleft()) # file input

    else:
        metadatas = [0 for x in range(children_cnt)]

        for x in range(children_cnt):
            # spawn children
            metadatas[x] = node( int(list_of_things.popleft()), int(list_of_things.popleft()), list_of_things ) #replace with next two inputs
        
        # print(metadatas)

        for x in range(metadata_cnt):
            # need to build table?
            idx = int(list_of_things.popleft())
            if idx <= children_cnt:
                # print(idx-1, metadatas[idx-1])
                metadata_sum += metadatas[idx-1]
    
    # print(metadata_sum)
    # print(list_of_things)

    return metadata_sum

def main():
    file = open(sys.argv[1], 'r')
    inputs = file.read()
    list = deque(inputs.split())

    print("Metadata sum = ", node( int(list.popleft()), int(list.popleft()), list ) )


main()