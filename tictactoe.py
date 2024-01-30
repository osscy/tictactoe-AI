
def checkWinnerHoriz(board, max, min):
    for row in board:
        brick = []
        for place in row:
            brick.append(place)
        if brick[0] == max and brick[1] == max and brick[2] == max:
            return True, max
        elif brick[0] == min and brick[1] == min and brick[2] == min:
            return True, min
    return False, None


def checkWinnerDiagonal(board, max, min):
    if board[0][0] == max and board[1][1] == max and board[2][2] == max:
        return True, max
    elif board[0][0] == min and board[1][1] == min and board[2][2] == min:
        return True, min
    elif board[0][2] == max and board[1][1] == max and board[2][0] == max:
        return True, max
    elif board[0][2] == min and board[1][1] == min and board[2][0] == min:
        return True, min

    return False, None


def checkWinnerVerti(board, max, min):
    brick = []
    # check each column
    for num in range(len(board)):
        for row in board:
            brick.append(row[num])
        if brick[0] == max and brick[1] == max and brick[2] == max:
            return True, max
        elif brick[0] == min and brick[1] == min and brick[2] == min:
            return True, min
        brick.clear()
    # return false if no winner
    return False, None


def evaluateGame(boardGame, max, min):
    gameEnd, player = checkWinnerHoriz(boardGame, max, min)
    if gameEnd:
        return player
    gameEnd, player = checkWinnerDiagonal(boardGame, max, min)
    if gameEnd:
        return player
    gameEnd, player = checkWinnerVerti(boardGame, max, min)
    if gameEnd:
        return player


def minmax(board, is_maximazer):
    # check for the winner, it will evaluate the board
    maxplayer = "X"
    minplayer = "O"

    winner = evaluateGame(board, maxplayer, minplayer)
    if winner == maxplayer:
        return 1
    elif winner == minplayer:
        return -1
    elif winner is None and all(pos != "" for row in board for pos in row):
        return 0

    if is_maximazer:
        maxeval = -80000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = maxplayer
                    # started with max player, thus next turn is minplayer.
                    ev = minmax(board, False)
                    board[row][col] = ""
                    # want higher value for maximizer
                    maxeval = max(maxeval, ev)
        return maxeval

    else:
        mineval = 8000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = minplayer
                    ev = minmax(board, True)
                    board[row][col] = ""
                    # want higher value for maximizer
                    mineval = min(mineval, ev)
        return mineval


def find_best_move(board):
    maxeval = -80000
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "X"
                eval = minmax(board, False)
                board[row][col] = ""

                if eval > maxeval:
                    maxeval = eval
                    best_move = (row, col)

    return best_move


def makeMoveMax(board):
    bestmove = find_best_move(board)
    #board[bestmove[0]][bestmove[1]] = "X"
    return bestmove


def checkPlace():
    number = True
    row = 0
    column = 0

    while number:
        row = int(input("Choose row: "))
        column = int(input("Choose column: "))
        if 0 <= row <= 2 and 0 <= column <= 2:
            number = False
        else:
            print("Number must be between 0 and 2")

    return row, column


def makeMoveMin(board, min):
    # min player makes move
    chose = True
    #row, column = checkPlace()

    while chose:
        if board[row][column] == "":
            board[row][column] = min
            chose = False
        else:
            print("Place already taken, choose another one!")
            row, column = checkPlace()

    return board

# The game


def playGame():
    max = "X"
    min = "O"

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    gameEnd = False
    print(board)

    while not gameEnd:

        print(f"player {min} turn")
        board = makeMoveMin(board, min)
        if evaluateGame(board, max, min) == "O":
            print(f"{min} is the winner")
            print(board)
            break
        print(board)

        print(f"player {max} turn")
        board = makeMoveMax(board)
        if evaluateGame(board, max, min) == "X":
            print(f"{max} is the winner")
            print(board)
            break
        print(board)
