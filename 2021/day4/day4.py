def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    values = file.readline().strip().split(',')
    boards = []

    while True:
        emptyLine = file.readline()
        if emptyLine == '':
            break

        board = []
        board.append(file.readline().split())
        board.append(file.readline().split())
        board.append(file.readline().split())
        board.append(file.readline().split())
        board.append(file.readline().split())
        boards.append(board)

    for i in range(1,len(values)):
        vals = values[0:i]
        for board in boards:
            if checkBoard(values=vals, board=board):
                # print(board)
                # print(vals)
                # print(vals[-1])
                total = 0
                for row in board:
                    total += sum(int(i) for i in row if i not in vals)

                print(total * int(vals[-1]))
                boards.remove(board)

def checkBoard(values, board):
    # check rows
    for row in board:
        allGood = True
        for val in row:
            if val not in values:
                allGood = False
        if allGood:
            return True

    # check columns
    for i in range(0,len(board[0])):
        allGood = True
        for j in range(0,len(board)):
            if board[j][i] not in values:
                allGood = False
        if allGood:
            return True


main()
