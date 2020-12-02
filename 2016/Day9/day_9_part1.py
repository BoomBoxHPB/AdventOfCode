import sys

def expand(in_str, paren_pos, recursive):
    x_pos = in_str.find("x", paren_pos)
    end_paren_pos = in_str.find(")", paren_pos)

    seq_len = int(in_str[paren_pos+1:x_pos])
    seq_rep = int(in_str[x_pos+1:end_paren_pos])

    curr_pos = end_paren_pos + 1
    total_seq_len = 0

    if recursive:
        while True:
            inner_paren_pos = in_str.find("(", curr_pos)
            if inner_paren_pos == -1 or inner_paren_pos > (end_paren_pos + seq_len):
                total_seq_len += ((end_paren_pos + seq_len + 1) - curr_pos)
                break
            new_inner_pos, inner_len = expand(in_str, inner_paren_pos, recursive)
            curr_pos = new_inner_pos
            total_seq_len += inner_len
    else:
        total_seq_len = seq_len

    #print(total_seq_len)
    total_seq_len = ( total_seq_len * seq_rep )

    return ( end_paren_pos + seq_len + 1 ), total_seq_len

def main():
    in_file = open(sys.argv[1], 'r')
    in_str = in_file.read()
    in_str_size = len(in_str)

    recursive = (sys.argv[2] == '2')

    curr_pos = 0
    char_cnt = 0

    while True:
        paren_pos = in_str.find("(", curr_pos)

        if paren_pos == -1:
            # EOF handling
            break

        char_cnt += ( paren_pos - curr_pos )

        curr_pos, total_seq_len = expand(in_str, paren_pos, recursive)

        char_cnt += total_seq_len

        #print('{}, {}'.format(paren_pos, end_paren_pos))
    print(char_cnt)

main()
