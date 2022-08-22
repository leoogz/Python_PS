import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int, readl().split())) for _ in range(K)]
    return R, C, K, rects


# 입력받는 부분
R, C, K, rects = input_data()


def draw_map(R, C, K, rec):
    map_paper = [[0 for _ in range(C)] for _ in range(R)]
    for r in rec:
        for i in range(r[1], r[3]):
            for j in range(r[0], r[2]):
                map_paper[i][j] = 2
    return map_paper


def dfs(r, c, map_paper, area):
    stk = deque()
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 1
    map_paper[r][c] = 1
    stk.append((r, c))
    while stk:
        cur_r, cur_c = stk.pop()

        for d in dir:
            nr = cur_r + d[0]
            nc = cur_c + d[1]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if map_paper[nr][nc] == 0:
                stk.append((nr, nc))
                map_paper[nr][nc] = 1
                cnt += 1

    area.append(cnt)
    return


def Solve(R, C, K, rec):
    cnt = 0
    area = []
    map_paper = draw_map(R, C, K, rec)
    for i in range(R):
        for j in range(C):
            if map_paper[i][j] == 0:
                cnt += 1
                dfs(i, j, map_paper, area)
    return cnt, sorted(area)


sol_cnt, sol_area = Solve(R, C, K, rects)
print(sol_cnt)
print(*sol_area)
