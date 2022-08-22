import sys
from collections import deque, defaultdict


def Input_Data():
    readl = sys.stdin.readline
    N, M, K = map(int, readl().split())
    info = [list(map(int, readl().split()))for _ in range(M)]
    return N, M, K, info


sol = -1
# 입력 받는 부분
N, M, K, info = Input_Data()

# 여기서부터 작성


def dfs(s, visit, conn):
    stk = deque()
    stk.append(s)
    cnt = 0
    while stk:
        p = stk.pop()
        for n in conn[p]:
            if visit[n] == 0:
                visit[n] = 1
                stk.append(n)
                cnt += 1
    return cnt


conn = defaultdict(list)
for s, e in info:
    conn[s].append(e)
    conn[e].append(s)
visit = [0 for _ in range(N+1)]
city = []

for i in range(1, N+1):
    if visit[i] == 0:
        city.append(dfs(i, visit, conn))
city.sort(reverse=True)
mx = 0
for i in range(K+1):
    if i < len(city):
        mx += city[i]
    else:
        mx += 1

if mx > N:
    mx = N
sol = mx

# 출력 하는 부분
print(sol)
