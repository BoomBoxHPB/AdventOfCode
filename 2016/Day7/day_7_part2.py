import sys

def aba(val):
    if( val[0] == val[2] and
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
        abas = []
        babs = []
        
        for i in range(len(chars) - 2):
            if chars[i] == '[':
                brackets = True
            elif chars[i] == ']':
                brackets = False
            else:
                is_aba = aba(chars[i:i+3])
                if is_aba and brackets:
                    babs.append(chars[i:i+3])
                elif is_aba and not brackets:
                    abas.append(chars[i:i+3])
        
        for i in abas:
            for j in babs:
                if i[0] == j[1] and i[1] == j[0]:
                    good_address = True
        
        if good_address:
            total_good_addressses += 1
    
    print( total_good_addressses )

main()