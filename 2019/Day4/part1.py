import sys

def main():
    file = open(sys.argv[1], 'r')
    code_range = file.readline().split('-')
    code_range = [int(x) for x in code_range]

    # print(code_range)    
    valid_codes = 0

    for code in range(code_range[0], code_range[1]+1):
        code_string = str(code)
        code_parts = [int(x) for x in code_string]
        # print(code_parts)

        order_valid = code_parts == sorted(code_parts)

        dupe_valid = False
        for x in range(5):
            if code_parts[x] == code_parts[x+1]:
                dupe_valid = True

        if order_valid and dupe_valid:
            valid_codes = valid_codes + 1

    print(valid_codes)

main()