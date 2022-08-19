import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int, readl().split())) +
                    [0] if 1 <= r <= N else [0] * (N+2) for r in range(N+2)]
    return N, r_top, c_top, map_mountine


sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()

# 여기서부터 작성


def Solve(r, c, m):
    _min = 1000000
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    q.append((r, c))
    cost = [[100000 for _ in range(N+2)]for _ in range(N+2)]
    cost[r][c] = 0
    while len(q):
        cur_r, cur_c = q.pop()
        if m[cur_r][cur_c] == 0:
            _min = min(_min, cost[cur_r][cur_c])
            continue
        for d in dir:
            nr = cur_r + d[0]
            nc = cur_c + d[1]
            height = m[nr][nc]
            if height <= m[cur_r][cur_c]:
                nt = (m[cur_r][cur_c] - height) ** 2
            else:
                nt = (m[cur_r][cur_c] - height)
            if cost[cur_r][cur_c] + nt < cost[nr][nc]:
                cost[nr][nc] = cost[cur_r][cur_c] + nt
                q.appendleft((nr, nc))

    return _min


sol = Solve(r_top, c_top, map_mountine)
# 출력하는 부분
print(sol)
