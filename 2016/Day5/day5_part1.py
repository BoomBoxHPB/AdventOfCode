import sys
import hashlib

def main():
    init_hash = open(sys.argv[1], 'r').readline()
    password = ""
    found = 0
    index = 0
    
    while found < 8:
        hash = hashlib.md5(bytearray(init_hash + str(index),'ascii')).hexdigest();
        if hash[0:5] == "00000":
            password += hash[5]
            found += 1
            print(password, ", Index = ", index)
        index += 1
        
    print(password)

main()