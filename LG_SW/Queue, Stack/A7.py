import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_cmd = [list(map(int, readl().split())) for _ in range(N)]
    return N, list_cmd
 
 
def Solve():
    q = deque()
    for cmd in list_cmd:
        if cmd[0] == 0:
            # 아래 코드 수정
            if q:
                print(q.popleft())
            else:
                print("E")
            pass
        elif cmd[0] == 1:
            # 아래 코드 수정
            q.append(cmd[1])
            pass
        elif cmd[0] == 2:
            # 아래 코드 수정
            print(len(q))
            pass
 
 
# 입력받는 부분
N, list_cmd = Input_Data()
 
Solve()