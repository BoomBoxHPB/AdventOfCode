import sys
import string

def main():
    file = open(sys.argv[1], 'r')
    inputs = file.readlines()
    worker_cnt = 5
    workers = [0 for x in range(worker_cnt)]
    for x in range(worker_cnt):
        workers[x] = ['',0]
    seq = []
    result = ""
    for line in inputs:
        pieces = line.split()
        # print(pieces)
        seq.append((pieces[1],pieces[7]))
    
    # print(seq)
    # print(seq[1])
    # print(seq[1][1])

    avail = []
    for x in seq:
        if not (x[0] in avail):
            avail.append(x[0])
        if not (x[1] in avail):
            avail.append(x[1]) 

    avail.sort()
    done_len = len(avail)
    # print(avail)

    seconds = 0 # 0 or 1?
    while done_len != len(result):
        # See if any workers are done this second
        for w in workers:
            if w[1] > 0:
                w[1] -= 1
                if w[1] == 0:
                    # Done, remove the entries
                    result += w[0]
                    while True:
                        something_removed = False
                        for x in seq:
                            if w[0] == x[0]:
                                # remove x from seq
                                seq.remove(x)
                                something_removed = True
                                break
                        if not something_removed:
                            break
                    w[0] = ''
                    # print(seq)

        for w in workers:
            if w[0] == '':
                for ch in avail:
                    restriction_found = False

                    for x in seq:
                        if ch == x[1]:
                            restriction_found = True
                            break
                    
                    if not restriction_found:
                        w[0] = ch
                        w[1] = string.ascii_uppercase.index(ch) + 1 + 60

                        # Assign ch to an available worker
                        avail.remove(ch)

                        # print(seq)
                        break
                
                if w[0] == '':
                    # Didn't find anything for this worker, don't bother with the
                    # other workers
                    break
            
        seconds += 1

        # print(seconds, workers)

    seconds -= 1
    print(result, seconds)

main()