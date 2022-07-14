import sys
from collections import *
 
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    R, C, S, K = map(int, readl().split())
    return N, M, R, C, S, K
 
 
sol = -1
# 입력 받는 부분
N, M, R, C, S, K = Input_Data()
 
# 여기서부터 작성
 
next = [(-2,-1),(-2,1),(-1,-2),(-1,2)]
board = [[0] + [0]*M + [0]]*(N+2)
visit = [[1] + [0]*M + [1] if 1<=n<=N else [1] * (M+2) for n in range(N+2)]
 
q = deque()
q.append((R,C))
visit[R][C] = 1
def check(q, move,r,c):
        if r < 1 or r > N:
            return False
        elif c < 1 or c > M:
            return False
        elif visit[r][c] == 0:
            q.append((r,c))
            visit[r][c] = move + 1
            return True
        else:
            return False
 
while len(q) != 0:
    curR, curC = q.popleft()
    move = visit[curR][curC]
    if (curR, curC) == (S,K):
        sol = move-1
        break
    for n in next:
        check(q,move,curR+n[0],curC+n[1])
        check(q,move,curR-n[0],curC-n[1])
 
 
# 출력하는 부분
 
print(sol)