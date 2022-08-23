import sys
from collections import defaultdict, deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cost = [[0] + list(map(int, readl().split())) if 1 <=
            n <= N else [0]*(N+1) for n in range(N+1)]
    return N, cost


# 입력받는 부분
N, cost = Input_Data()

# 여기서부터 작성
M = 99999
visit = [0]*(N+1)
sum = 0

result = []


def solve(n, sum, q):
    global M
    global result
    if sum > M:

        return
    if n < N+1:
        for i in range(1, N+1):
            if visit[i] == 0:
                visit[i] = cost[n][i]
                q.append(i)
                solve(n+1, sum + cost[n][i], q)
                q.pop()
                visit[i] = 0
            continue
    else:
        M = min(M, sum)
        result = list(q)
    return


q = deque()
solve(1, 0, q)
sol = M
# 출력하는 부분
print(sol)
print(*result)
