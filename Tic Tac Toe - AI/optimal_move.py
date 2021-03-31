from sys import maxsize as MAX

MAX_SCORE = 10
MIN_SCORE = -10


# check if there is any empty spot
def moveLeft(board):
    for row in board:
        if ' ' in row:
            return True

    return False


# check if anyone has won the game
def isFinished(board):
    for row in range(0, 3):

        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:

            if board[row][0] == 'O':
                return 10
            elif board[row][0] == 'X':
                return -10

    for col in range(0, 3):

        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:

            if board[0][col] == 'O':
                return 10
            elif board[0][col] == 'X':
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:

        if board[0][0] == 'O':
            return 10
        elif board[0][0] == 'X':
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:

        if board[0][2] == 'O':
            return 10
        elif board[0][2] == 'X':
            return -10

    return 0


# minimax implementation using alpha beta pruning
def minimax(board, depth=0, maximizer=True, alpha=-MAX, beta=MAX):

    winner = isFinished(board)
    if winner == 10:
        return winner - depth
    if winner == -10:
        return winner + depth
    if not moveLeft(board):
        return 0

    if maximizer:
        best = -MAX
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = minimax(board, depth + 1, False, alpha, beta)
                    best  = max(best, value)
                    alpha = max(alpha, best)
                    board[i][j] = ' '

                    if beta <= alpha:
                        return best
        return best

    else:
        best = MAX
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, depth + 1, True, alpha, beta)
                    best  = min(best, value)
                    beta  = min(beta, best)
                    board[i][j] = ' '

                    if beta <= alpha:
                        return best
        return best


# for each empty spot kick off the minimax
# and return the best move possible
def getOptimalMove(board):
    bestValue = -MAX
    bestMove = ()

    alpha, beta = -MAX, MAX
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                value = minimax(board, 0, False, alpha, beta)
                if value > bestValue:
                    bestValue = value
                    bestMove = (i, j)
                alpha = max(alpha, bestValue)
                board[i][j] = ' '

    return bestMove
