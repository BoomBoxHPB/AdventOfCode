import sys

def abba(val):
    if( val[0] == val[3] and
        val[1] == val[2] and
        val[0] != val[1] ):
        return True
    else:
        return False

def main():
    file = open(sys.argv[1], 'r')
    addresses = file.readlines()
    total_good_addressses = 0
    
    for address in addresses:
        chars = list(address)
        brackets = False
        good_address = False
        
        for i in range(len(chars) - 3):
            if chars[i] == '[':
                brackets = True
            elif chars[i] == ']':
                brackets = False
            else:
                is_abba = abba(chars[i:i+4])
                if is_abba and brackets:
                    good_address = False
                    break
                elif is_abba and not brackets:
                    good_address = True
            
        if good_address:
            total_good_addressses += 1
    
    print( total_good_addressses )

main()