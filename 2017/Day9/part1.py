import sys

chars = list(open(sys.argv[1], 'r').readline())
curr_level = 0
total_score = 0
skip_next = False
open_garbage = False
garbage_cnt = 0

for c in chars:
    if skip_next:
        skip_next = False
        continue
    elif c == '!':
        skip_next = True
        continue
    elif open_garbage:
        if c == '>':
            open_garbage = False
        else:
            garbage_cnt += 1            
        continue
    elif c == '<':
        open_garbage = True
        continue
    elif c == ',':
        # Blindly assuming these don't really matter...
        continue
    # The good stuff
    elif c == '{':
        curr_level += 1
        total_score += curr_level
    elif c == '}':
        curr_level -= 1

print(total_score)
print(garbage_cnt)