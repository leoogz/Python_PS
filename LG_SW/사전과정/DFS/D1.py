import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
M = 99999
visit = [0]*(N+1)
sum = 0


def solve(n,sum):
    global M
    if sum > M: return
    if n < N+1:
        for i in range(1,N+1):
            if visit[i] == 0:
                visit[i] = matrix[n][i]
                solve(n+1,sum + matrix[n][i])
                visit[i] = 0
            continue
    else:
        if sum < M:
            M = sum
    return

solve(1,0)
sol = M
# 출력하는 부분
print(sol)