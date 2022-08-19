import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    L = int(readl())
    N = int(readl())
    dist = [0] + list(map(int, readl().split()))
    time = [0] + list(map(int, readl().split())) + [0]
    return L, N, dist, time


# 입력받는 부분
L, N, dist, time = Input_Data()
_min = [0] + [100000] * (N+1)
station = [[] for _ in range(N+2)]

for i in range(1, N+2):
    dist[i] += dist[i-1]


for i in range(1, N+2):
    for j in range(i-1, -1, -1):
        if dist[i] - dist[j] <= L and _min[i] > _min[j]+time[i]:
            _min[i] = _min[j] + time[i]
            station[i] = station[j] + [i]
r = station[-1][:-1:]

print(_min[-1])
print(len(r))
print(*r)
