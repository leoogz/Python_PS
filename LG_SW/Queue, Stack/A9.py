import sys
from collections import deque
 
 
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job
 
 
T = int(sys.stdin.readline())
sol = []
q = deque()
for _ in range(T):
    # 입력받는 부분
    N, M, job = Input_Data()
    # 여기서부터 작성
    num = 0
    q.clear()
    for i in range(0,N):
        q.append((i,job[i]))
    while q:
        flg = False
        for i in range(1,N):
            if q[0][1] < q[i][1]:
                q.append(q.popleft())
                flg = True
                break
        if flg:
            pass
        else:
            num += 1
            if M == q[0][0]:
                sol.append(num)
                break
            q.popleft()
            N -= 1
  
 
 
# 출력하는 부분
print(*sol, sep='\n')