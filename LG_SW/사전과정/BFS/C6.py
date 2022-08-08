import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix


sol = -1
route = deque()
# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
q = deque()
best = [0] + [99999] * N
path = [0] + [0]*N
q.append((1,0))
best[1] = 0
while q:
    p, time = q.popleft()
    if best[p] < time:
        continue
    for i in range(1,N+1):
        if i == p:
            continue
        if matrix[p][i] + time <= best[i]:
            best[i] = matrix[p][i] + time
            q.append((i,best[i]))
            path[i] = p
            

# 여기서부터 작성
n = M
route.appendleft(n)
while n != 1:
    n = path[n]
    route.appendleft(n)
sol = best[M]
# 출력하는 부분
print(sol)
print(*list(route))

