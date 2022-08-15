import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num


sol = -1
# 입력받는 부분
N, K, num = Input_Data()

# 여기서부터 작성
stack = deque()
idx = 0
stack.append(num[idx])
cnt = 0
for idx in range(1, N):
    if cnt >= K:
        stack.appendleft(num[idx])
        continue
    while num[idx] > stack[0]:
        stack.popleft()
        cnt += 1
        if len(stack) == 0 or cnt >= K:
            break
    if len(stack) >= N-K:
        continue
    stack.appendleft(num[idx])

# 출력하는 부분
sol = ''.join(list(stack)[::-1])

print(int(sol))
