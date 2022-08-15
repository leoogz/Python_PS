import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    names = [readl().strip() for _ in range(N)]
    return N, K, names


sol = -1

# 입력 받는 부분
N, K, names = Input_Data()

# 여기서부터 작성
cnt = 0
stk = [deque() for _ in range(21)]
for i in range(N):
    l = len(names[i])
    while len(stk[l]) and stk[l][0] + K < i:
        stk[l].popleft()

    cnt += len(stk[l])
    stk[l].append(i)

sol = cnt
# 출력하는 부분
print(sol)
