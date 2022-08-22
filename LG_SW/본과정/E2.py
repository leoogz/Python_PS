import sys
from collections import deque
import math


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    n = 2000001
    map_field = [[n] + list(map(int, readl().split())) + [n]
                 if 1 <= r <= N else [n] * (N+2) for r in range(N+2)]
    return N, map_field


sol = -1000000
# 입력받는 부분
N, map_field = Input_Data()

# 여기서부터 작성
_max = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        _max = max(_max, map_field[i][j])


def flood_fill(r, c, D, visit):
    cnt = 1
    stk = deque()
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visit[r][c] = 1
    stk.append((r, c))
    while stk:
        cur_r, cur_c = stk.pop()
        for d in dir:
            nr = cur_r + d[0]
            nc = cur_c + d[1]
            if abs(map_field[nr][nc] - map_field[cur_r][cur_c]) <= D and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                stk.append((nr, nc))
                cnt += 1
    return cnt


def dfs(D):
    cnt = 0
    visit = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visit[i][j]:
                continue
            cnt = flood_fill(i, j, D, visit)
            if cnt >= round(N**2/2):
                return True
    return False


s = 0
e = _max
while s < e:
    d = (s + e)//2
    if dfs(d):
        e = d
    else:
        s = d + 1

if s == e:
    D = (s + e)//2
    if dfs(D):
        d = D

sol = d
# 출력하는 부분
print(sol)
