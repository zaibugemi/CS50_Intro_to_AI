"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state():
        return X
    elif board == terminal(board):
        return 'over'
    else:
        Xs, Os = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    Xs += 1
                elif board[i][j] == O:
                    Os += 1
        if Xs == Os:
            return X
        elif Os < Xs:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if board == terminal(board):
        return 'over'
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise ValueError('Invalid Action')

    cpy = copy.deepcopy(board)
    cpy[action[0]][action[1]] = player(board)

    return cpy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if ((board[0][0] == X and board[0][1] == X and board[0][2] == X) or
            (board[1][0] == X and board[1][1] == X and board[1][2] == X) or
            (board[2][0] == X and board[2][1] == X and board[2][2] == X) or
            (board[0][0] == X and board[1][0] == X and board[2][0] == X) or
            (board[0][1] == X and board[1][1] == X and board[2][1] == X) or
            (board[0][2] == X and board[1][2] == X and board[2][2] == X) or
            (board[0][0] == X and board[1][1] == X and board[2][2] == X) or
            (board[2][0] == X and board[1][1] == X and board[0][2] == X)):
        return X
    elif ((board[0][0] == O and board[0][1] == O and board[0][2] == O) or
            (board[1][0] == O and board[1][1] == O and board[1][2] == O) or
            (board[2][0] == O and board[2][1] == O and board[2][2] == O) or
            (board[0][0] == O and board[1][0] == O and board[2][0] == O) or
            (board[0][1] == O and board[1][1] == O and board[2][1] == O) or
            (board[0][2] == O and board[1][2] == O and board[2][2] == O) or
            (board[0][0] == O and board[1][1] == O and board[2][2] == O) or
            (board[2][0] == O and board[1][1] == O and board[0][2] == O)):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
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
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = (-1, None)
        for action in actions(board):
            min_val = min_value(result(board, action))
            val = max(v[0], min_val)
            if val == min_val:
                v = (min_val, action)

        return v[1]

    if player(board) == O:
        v = (1, None)
        for action in actions(board):
            max_val = max_value(result(board, action))
            val = min(v[0], max_val)
            if val == max_val:
                v = (max_val, action)
        return v[1]


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = 1
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
