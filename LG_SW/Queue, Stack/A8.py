import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N
 
 
sol = []
# 입력 받는 부분
N = Input_Data()
q = deque()
for i in range(N,0,-1):
    q.append(i)
 
for i in range(1,N):
    p = int(q[0]/2)
    for j in range(0,p):
        q.appendleft(q.pop())
    sol.append(q.pop())
# 여기서부터 작성
 
sol.append(q.pop())
# 출력하는 부분
print(*sol)