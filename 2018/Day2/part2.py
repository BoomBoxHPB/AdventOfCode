import sys

def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()

    for first in range(len(lines)-1):
        first_str = lines[first]
        str_len = len(first_str)
        for second in range(first+1, len(lines)):
            diffs = 0;
            second_str = lines[second]
            for ch_idx in range(str_len):
                if first_str[ch_idx] != second_str[ch_idx]:
                    diffs += 1
            if diffs == 1:
                new_str = ""
                for ch_idx in range(str_len):
                    if first_str[ch_idx] == second_str[ch_idx]:
                        new_str += first_str[ch_idx]
                print( "Common = ", new_str )
                return

main()