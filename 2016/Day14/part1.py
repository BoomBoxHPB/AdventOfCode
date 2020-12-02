import hashlib

class quick_hash():
    m_list = {} # Don't want to recompute the hash...

    def get_index(self, i):
        if not i in self.m_list:
            m = hashlib.md5()
            magic = 'ahsbgdzn' # 'abc'
            hash_i = magic + str(i)
            m.update(bytearray(hash_i, 'utf-8'))
            self.m_list[i] = m.hexdigest()

            # Part 2 only!
            for j in range(2016):
                temp = bytearray(m.hexdigest(), 'utf-8')
                m = hashlib.md5()
                m.update(temp)

            self.m_list[i] = m.hexdigest()

        return self.m_list[i]

i = 0
found = 0
qh = quick_hash()

# print(qh.get_index(0))
while found < 64:
    the_char = ''
    h = qh.get_index(i)
    for j in range(len(h) - 2):
        if h[j] == h[j+1] == h[j+2]:
            the_char = h[j]
            break

    if the_char != '':
        thingy = the_char + the_char + the_char + the_char + the_char

        for j in range(i+1, i+1001):
            if thingy in qh.get_index(j):
                found += 1
                break
    
    if found < 64:
        i += 1

print("64th index is", i)
