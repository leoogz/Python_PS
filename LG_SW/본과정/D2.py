import sys
from collections import deque


def Input_Data():
    R, C = map(int, readl().split())
    map_forest = [[0] + list(readl()[:-1]) + [0] if 1 <=
                  r <= R else [0]*(C+2) for r in range(R+2)]
    return R, C, map_forest


readl = sys.stdin.readline

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def read_map(R, C, m):
    D = ()
    S = ()
    F = deque()
    for i in range(1, R+1):
        for j in range(1, C+1):
            t = m[i][j]
            if t == 'S':
                S = [i, j, 0]
            elif t == 'D':
                D = (i, j)
            elif t == '*':
                F.append((i, j))

    return D, S, F


def flood(F, m):
    l = len(F)
    for i in range(l):
        f = F.pop()
        for d in dir:
            nR = f[0] + d[0]
            nC = f[1] + d[1]
            if m[nR][nC] == '.' or m[nR][nC] == 'D':
                m[nR][nC] = '*'
                F.appendleft((nR, nC))
    return


def Solve(R, C, m):
    cnt = 0
    stk = deque()
    D, S, F = read_map(R, C, m)
    stk.appendleft(S)
    cnt = -1
    while len(stk):
        cR, cC, cT = stk.pop()
        if cnt != cT:
            flood(F, m)
            cnt = cT
        for d in dir:
            nR = cR + d[0]
            nC = cC + d[1]
            if m[nR][nC] == '.':
                stk.appendleft([nR, nC, cT+1])
                m[nR][nC] = 'S'
            if m[nR][nC] == 'D':
                return cT+1

    return -1


T = int(readl())
for _ in range(T):
    # 입력받는 부분
    R, C, map_forest = Input_Data()

    sol = Solve(R, C, map_forest)
    if sol == -1:
        print("KAKTUS")
    else:
        print(sol)
    # 여기서부터 작성
