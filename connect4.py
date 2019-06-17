# initialize new board
def createBoard():
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    return board


# print board
def printBoard():
    print("0\t1\t2\t3\t4\t5\t6\n--------------------------")
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            print(newBoard[i][j],end='\t')
        print('')


# check horizontal if player wins
def checkHorizontal(player):
    p_i = 999
    p_j = 999
    counter = 0
    wins = False
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] == player:
                if counter == 0:
                    p_i = i
                    p_j = j
                    counter += 1
                else:
                    if i == p_i and j - 1 == p_j:
                        counter += 1
                        p_j = j
                    else:
                        counter = 0
                if counter == 4:
                    wins = True
    return wins


# check vertical if player wins
def checkVertical(player):
    p_i = 999
    p_j = 999
    counter = 0
    wins = False
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] == player:
                if counter == 0:
                    p_i = i
                    p_j = j
                    counter += 1
                else:
                    if j == p_j and i - 1 == p_i:
                        counter += 1
                        p_i = i
                    else:
                        counter = 0
                if counter == 4:
                    wins = True
    return wins


# check diagonal if player wins
def checkDiagonal(player):
    p_i = 999
    p_j = 999
    counter = 0
    wins = False
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] == player:
                if counter == 0:
                    p_i = i
                    p_j = j
                    counter += 1
                else:
                    if (i - 1 == p_i and j - 1 == p_j) or (i + 1 == p_i and j + 1 == p_j) or (i + 1 == p_i and j - 1 == p_j) or (i - 1 == p_i and j + 1 == p_j):
                        counter += 1
                        p_i = i
                        p_j = j
                    else:
                        counter = 0
                if counter == 4:
                    wins = True
    return wins


# player makes play
def player(player):
    return int(input("Player " + str(player) + " input from 0-6: "))


# modify board
def modifyBoard(player, player_inp):
    row = len(newBoard) - 1
    col = player_inp
    found_slot = False
    while not found_slot:
        if newBoard[row][col] == 0:
            newBoard[row][col] = player
            found_slot = True
        else:
            if row != 0:
                row -= 1
            else:
                col = int(input(
                    "Player " + str(player) + " please choose another column other than " + str(player_inp) + ": "))


newBoard = createBoard()
game_over = False
turn = 0

#play game
print("Welcome to connect four!!!\n===========================")
while not game_over:
    printBoard()
    # player 1 turn:
    if turn == 0:
        p1 = player(1)
        modifyBoard(1, p1)
        printBoard()
        if checkHorizontal(1) or checkVertical(1) or checkDiagonal(1):
            print("Player 1 Wins!!!")
            break
        turn = 1
    # player 2 turn:
    if turn == 1:
        p2 = player(2)
        modifyBoard(2, p2)
        printBoard()
        if checkHorizontal(2) or checkVertical(2) or checkDiagonal(2):
            print("Player 2 Wins!!!")
            break
        turn = 0
    # game_over = True
