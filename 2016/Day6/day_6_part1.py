import sys

def main():
    file = open(sys.argv[1], 'r')
    entries = file.readlines()
    letter_count = []
    result = ""
    
    for line in entries:
        letters = list(line)
        iter_count = 0
        
        for i in letters:
            if len(letter_count) <= iter_count:
                letter_count.append({})
            
            if i in letter_count[iter_count]: letter_count[iter_count][i] += 1
            else: letter_count[iter_count][i] = 1
            iter_count += 1
            
    for i in range(len(letter_count)):
        sorted_letters = sorted(letter_count[i].items(), key=lambda x: x[1], reverse=True )
        result += sorted_letters[0][0]
    
    print( result )

main()