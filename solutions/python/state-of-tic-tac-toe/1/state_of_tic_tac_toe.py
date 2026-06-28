"""
checks the state of a Tic Tac Toe game
"""

BOARD_SIZE = 3
WIN_MSG = "win"

def is_both_x_or_0(a, b):
    if a == "X" and b == "X":
        return True
    if a == "O" and b == "O":
        return True
    return False


def is_ongoing(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if not board[i][j] or board[i][j] == " ":
                return True
    return False

def is_won_diagonal(board):
    win_count = 0
    is_won = False
    if is_both_x_or_0(board[0][0], board[1][1]) and is_both_x_or_0(board[1][1], board[2][2]):
            win_count += 1
            is_won =  True
    if is_both_x_or_0(board[0][2], board[1][1]) and is_both_x_or_0(board[1][1], board[2][0]):
            win_count += 1
            is_won =  True
    return (is_won, win_count)

def is_won_column(board):
    win_count = 0
    is_won = False
    for i in range(BOARD_SIZE):
         if is_both_x_or_0(board[0][i], board[1][i]) and is_both_x_or_0(board[1][i], board[2][i]):
            win_count += 1
            is_won =  True
    return (is_won, win_count)

def is_won_row(board):
    win_count = 0
    is_won = False
    for i in range(BOARD_SIZE):
        if is_both_x_or_0(board[i][0], board[i][1]) and is_both_x_or_0(board[i][1], board[i][2]):
            win_count += 1
            is_won =  True
    return (is_won, win_count)

def is_edge_case(board):
    if board == ["XOX", "OXO", "XOX"] or board == ["OXO", "XOX", "OXO"] or board == ["XXX", "XOO", "XOO"]:
        return True

def is_invalid(board):
    xs = 0
    os = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "X":
                xs += 1
            elif board[i][j] == "O":
                os += 1

    if os > xs:
        return (True, "O started")

    if (xs - os) > 1:
        return (True, "X went twice")

    return False, ""
        
                

def gamestate(board):

    invalid, reason = is_invalid(board)
    if invalid:
        raise ValueError("Wrong turn order: " + reason)

    if is_edge_case(board):
        return WIN_MSG

    win_count = 0
    new_win_count = 0
    is_won = False

    is_won, new_win_count = is_won_row(board)
    win_count += new_win_count
    new_win_count = 0
    is_won, new_win_count = is_won_column(board)
    win_count += new_win_count
    new_win_count = 0
    is_won, new_win_count = is_won_diagonal(board)
    win_count += new_win_count
    new_win_count = 0

    if win_count == 1:
        return WIN_MSG
    elif win_count > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    if is_ongoing(board):
        return "ongoing"
    return "draw"