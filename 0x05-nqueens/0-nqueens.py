#!/usr/bin/python3
"""
Solve the N Queens challenge
"""
import sys


def threat(board, row, col, num):
    """
    Check if placing a queen will be a threat
    """
    for i in range(col):
        if board[row][i] == 1:
            return True
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True
    for i, j in zip(range(row, num, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True
    return False


def solve(board, col, num):
    """
    Backtrack to find every possible board configuration
    """
    if col == num:
        solution = []
        for i in range(num):
            for j in range(num):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    for i in range(num):
        if not threat(board, i, col, num):
            board[i][col] = 1
            solve(board, col + 1, num)
            board[i][col] = 0


def check_N():
    """
    Check if N is valid
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)


if __name__ == "__main__":
    check_N()
    num = int(sys.argv[1])
    board = [[0 for _ in range(num)] for _ in range(num)]
    solve(board, 0, num)
