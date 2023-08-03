#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem using backtracking
    """
    if N < 4:
        return

    board = [-1 for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
