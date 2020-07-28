"""
Tic Tac Toe Player
"""

import math
import copy
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt = 0
    num = 0
    if board == initial_state():
        return X
    else:
        for i in range(3):
            for j in range(3):
                if (board[i][j] == 'X'):
                    cnt = cnt+1
                elif (board[i][j] == "O"):
                    num = num+1
    if cnt > num:
        return O
    elif not terminal(board) and cnt == num:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    S = set()
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                S.add((i, j))
    return S


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = deepcopy(board)
    A = player(new_board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action.")
    else:
        new_board[i][j] = A

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0] == ["X", "X", "X"]
        or board[1] == ["X", "X", "X"]
        or board[2] == ["X", "X", "X"]
        or board[0][0] == board[1][0] == board[2][0] == "X"
        or board[0][1] == board[1][1] == board[2][1] == "X"
        or board[0][2] == board[1][2] == board[2][2] == "X"
        or board[0][0] == board[1][1] == board[2][2] == "X"
            or board[0][2] == board[1][1] == board[2][0] == "X"):
        return X
    if (board[0] == ["O", "O", "O"]
        or board[1] == ["O", "O", "O"]
        or board[2] == ["O", "O", "O"]
        or board[0][0] == board[1][0] == board[2][0] == "O"
        or board[0][1] == board[1][1] == board[2][1] == "O"
        or board[0][2] == board[1][2] == board[2][2] == "O"
        or board[0][0] == board[1][1] == board[2][2] == "O"
            or board[0][2] == board[1][1] == board[2][0] == "O"):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == 'X' or winner(board) == 'O':
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    W = winner(board)
    if W == "X":
        utility_ = 1
    elif W == "O":
        utility_ = -1
    else:
        utility_ = 0

    return utility_


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v
"""
def minimax(board):

    
    p = player(board)

    # If empty board is provided as input, return corner.
    #new_state = None
    #states = actions(board)
    temporary = deepcopy(board)
    #new_score = 0
    #old_score = 0
   
    if p == X:
        
            #temporary[i][j] = "X"
        old_score=float("-inf")
        new_state = None
        for state in action(board):
                
            new_score = minvalue(result(board,state))
            if new_score > old_score:
                old_score = new_score
                new_state = state
    elif p==O:
            #temporary[i][j] = "O"
        old_score=float("inf")
        new_state = None
        for state in actions(board):
            
            new_score1 = maxvalue(result(board,state))
            if new_score1 < old_score:
                old_score = new_score1
                new_state = state
    #board = temporary
    return new_state
"""

def minimax(board):
    
    #Returns the optimal action for the current player on the board.
    
    new_state = None
    p=player(board)
    #states = actions(board)
    #temporary = deepcopy(board)
    #new_score = 0
    old_score = -9999
    old_score1=9999
    for state in actions(board):
        #i, j = state

        if p == X:
            #old_Score=float("-inf")
            #new_state = None
            new_score = minvalue(result(board,state))
            if new_score > old_score:
                old_score = new_score
                new_state = state
        elif p==O:
            #old_score1=float("inf")
            #new_state = None
            new_score1 = maxvalue(result(board,state))
            if new_score1 < old_score1:
                old_score1 = new_score1
                new_state = state
    #board = temporary
    return new_state
























