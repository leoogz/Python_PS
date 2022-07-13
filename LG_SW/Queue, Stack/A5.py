import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height
 
 
 
 
# 입력받는 부분 
N, height = Input_Data()
sol_list = [0]*N
stack = deque()
# 여기서부터 작성
for i in range(0,N):
    if stack:
        while True:
            p = stack.pop()
            if p[1] < height[i]:
                sol_list[p[0]] = i+1
                if stack:
                    pass
                else:
                    stack.append((i,height[i]))
            else:
                stack.append(p)
                stack.append((i,height[i]))
                break
    else:
        stack.append((i,height[i]))
 
 
# 출력하는 부분
print(*sol_list, sep='\n')