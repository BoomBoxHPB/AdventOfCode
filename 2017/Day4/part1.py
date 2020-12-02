import sys

lines = open(sys.argv[1], 'r').readlines()
valid_count = 0

for passphrase in lines:
    dupe_found = False
    passes = []

    # print(passphrase)
    words = passphrase.split()

    # print(words)
    for word in words:
        # Only sort for part 2
        new_word = ''.join(sorted(word))
        # new_word = word

        if new_word in passes:
            dupe_found = True
            continue
        passes.append(new_word)
        # print(passes)

    if not dupe_found:
        valid_count += 1

print(valid_count)