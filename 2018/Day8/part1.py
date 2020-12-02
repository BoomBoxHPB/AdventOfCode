import sys
from collections import deque

def node(children_cnt, metadata_cnt, list_of_things):
    metadata_sum = 0
    
    for x in range(children_cnt):
        # spawn children
        metadata_sum += node( int(list_of_things.popleft()), int(list_of_things.popleft()), list_of_things ) #replace with next two inputs
    
    for x in range(metadata_cnt):
        metadata_sum += int(list_of_things.popleft()) # file input
    
    return metadata_sum

def main():
    file = open(sys.argv[1], 'r')
    inputs = file.read()
    list = deque(inputs.split())

    print("Metadata sum = ", node( int(list.popleft()), int(list.popleft()), list ) )


main()