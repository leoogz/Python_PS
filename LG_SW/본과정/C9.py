import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0]
                    if 1 <= r <= R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling


sol_time, sol_zergling = -1, -1

# 입력받는 부분
C, R, sc, sr, map_zergling = Input_Data()


# 여기서부터 작성
stk = deque()
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visit = [[0 for _ in range(C + 2)]for _ in range(R + 2)]
stk.append((sr, sc))
visit[sr][sc] = 1

t_cnt = 0

for n in map_zergling:
    for a in n:
        if a:
            t_cnt += 1
cnt = 1
while len(stk):
    pr, pc = stk.pop()
    for d in dir:
        nc = pc + d[1]
        nr = pr + d[0]
        if map_zergling[nr][nc] != 0 and visit[nr][nc] == 0:
            visit[nr][nc] = visit[pr][pc] + 1
            cnt += 1
            stk.appendleft((nr, nc))

sol_time = visit[pr][pc] + 2
sol_zergling = t_cnt - cnt

# 출력하는 부분
print(sol_time, sol_zergling, sep='\n')
