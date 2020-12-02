import sys

def main():
    file = open(sys.argv[1], 'r')
    row_count = 0
    good_count = 0
    entries = file.readlines()
    sum_of_sectors = 0
    
    for line in entries:
        words = line.split('-')
        joined_str = ''.join(words[0:len(words)-1])
        shifted_str = ''
        last_word = words[len(words)-1]
        sector_value = int(last_word[0:3])
        letters = {}
        key = ''
        for i in joined_str:
            if i in letters: letters[i] += 1
            else: letters[i] = 1
            temp_i = i
            for n in range(sector_value):
                if temp_i == 'z':
                    temp_i = 'a'
                else:
                    temp_i = chr(ord(temp_i) + 1)
            shifted_str += temp_i
        
        # Sort alphabetically, then by value
        s_letters = sorted(letters.items())
        s_letters = sorted(s_letters, key=lambda x: x[1], reverse=True )

        # Form and check key
        for i in range(5):
            key += s_letters[i][0]
        if key == last_word[4:9]:
            sum_of_sectors += sector_value
            if shifted_str[0:len('northpole')] == 'northpole':
                print( "North Pole: ", sector_value)
    
    print( "Total sectors: ", sum_of_sectors )
main()