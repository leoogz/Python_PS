import sys
import copy


def input_data():
    readl = sys.stdin.readline
    return [list(map(int, readl().split())) for _ in range(9)]


# 입력받는 부분
sudoku = input_data()

# 여기서부터 작성


def check_line(r, c):

    cand = [x for x in range(1, 10)]
    for i in range(9):
        if sudoku[r][i] in cand:
            cand.remove(sudoku[r][i])
        elif sudoku[i][c] in cand:
            cand.remove(sudoku[i][c])

    y = 3*(r//3)
    x = 3*(c//3)
    for i in range(y, y+3):
        for j in range(x, x+3):
            if sudoku[i][j] in cand:
                cand.remove(sudoku[i][j])

    return cand


def fill_sudoku(n, z):
    if n == len(z):
        for r in sudoku:
            print(*r)
        return
    r, c = z[n]
    cand = check_line(r, c)

    for i in cand:
        sudoku[r][c] = i
        fill_sudoku(n+1, z)
    sudoku[r][c] = 0
    return


def Solve():
    z = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]
    fill_sudoku(0, z)
    return


Solve()
