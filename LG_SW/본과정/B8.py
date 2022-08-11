import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, C = map(int, readl().split())
    M = int(readl())
    info = [list(map(int, readl().split())) for _ in range(M)]
    return N, C, M, info


sol = 0

# 입력받는 부분
N, C, M, info = Input_Data()

dq = deque()

cnt = 0
# 여기서부터 작성
info.sort(key=lambda x: (x[1], x[0]))
a = [C for _ in range(N+1)]
for n in info:
    mn = C
    for i in range(n[0], n[1]):
        mn = min(mn, a[i])
    mn = min(mn, n[2])
    cnt += mn
    for i in range(n[0], n[1]):
        a[i] -= mn

sol = cnt
# 출력하는 부분
print(sol)
