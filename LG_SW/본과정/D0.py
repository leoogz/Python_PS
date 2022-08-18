import sys
from types import BuiltinFunctionType


def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_game = [readl().strip() for _ in range(R)]
    return R, C, map_game


def find_RB(R, C, map_game):
    red = ()
    blue = ()
    for i in range(1, R+1):
        for j in range(1, C+1):
            if map_game[i][j] == 'R':
                red = (i, j)
            elif map_game[i][j] == 'B':
                blue = (i, j)
            elif len(red) and len(blue):
                return red, blue
    return red, blue


def Solve(R, C, map_game):
    cnt = 0
    visit = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
    red, blue = find_RB(R, C, map_game)
    rR, rC = red
    bR, bC = blue
    return cnt


sol = []
T = int(input())
for t in range(T):
    # 입력받는 부분
    R, C, map_game = Input_Data()
    sol.append(Solve(R, C, map_game))
    # 작성하는 부분


# 출력하는 부분
print(*sol, sep='\n')
