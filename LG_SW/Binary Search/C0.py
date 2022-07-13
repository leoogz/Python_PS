import sys
from bisect import *
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos
 
 
sol = -1
# 입력받는 부분
N, pos = Input_Data()
 
def solve(N,pos):
    sol = 0
    for i in range(N):
        for j in range(i+1,N):
            tmp = pos[j] - pos[i]
            h  = 2 * tmp + pos[j]
            l = tmp + pos[j]
            low = bisect_left(pos,l)
            if low != N:
                high = bisect_right(pos,h)
                sol+=high - low
            else:
                sol += 0
    return sol
 
 
# 여기서부터 작성
pos.sort()
sol = solve(N,pos)
# 출력하는 부분
print(sol)