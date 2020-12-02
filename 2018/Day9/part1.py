import sys

def main():
    # file = open(sys.argv[1], 'r')
    # lines = file.readlines()

    marbles = [0]
    player_count = 404
    scores = [0 for x in range(player_count)]
    last_marble = 71852 *100
    idx = 0
    marble_num = 1
    curr_player = 1

    # Testing
    while True:
        if marble_num % 23 == 0:
            scores[curr_player-1] += marble_num
            idx -= 7 # move back 7
            if idx < 0:
                idx = len(marbles) + idx
            # remove a marble
            removed_marble = marbles.pop(idx)
            if idx == len(marbles):
                idx = 0
            # add to the current players score
            scores[curr_player-1] += removed_marble
        else:
            idx += 2
            if idx > len(marbles):
                idx = 1
            marbles.insert(idx,marble_num)

        if (marble_num == last_marble):
            print(max(scores))
            return

        if (marble_num % 1000) == 0:
            print(marble_num)

        #testing 
        # print("[", curr_player, "]", marbles )
        marble_num += 1
        curr_player %= player_count
        curr_player += 1


main()