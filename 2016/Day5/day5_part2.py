import sys
import hashlib

def main():
    init_hash = open(sys.argv[1], 'r').readline()
    password = list("xxxxxxxx")
    found = 0
    index = 0
    
    while found < 8:
        hash = hashlib.md5(bytearray(init_hash + str(index),'ascii')).hexdigest();
        if hash[0:5] == "00000":
            position = int(hash[5],16)
            if position < 8 and password[position] == 'x':
                password[position] = hash[6]
                found += 1
                print("".join(password), ", Index = ", index)
        index += 1
        
    print("".join(password))

main()