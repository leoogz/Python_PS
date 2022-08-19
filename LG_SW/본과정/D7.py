import sys
from collections import deque, defaultdict
import math


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [map(int, readl().split()) for _ in range(M)]
    return N, M, edges


sol = -1

# 입력받는 부분
N, M, edges = Input_Data()

# 여기서부터 작성

'''
def get_shortest_path(short, p):
    _min = 99999
    q = deque()

    q.appendleft(N)
    cost = [99999 for _ in range(N+1)]
    cost[N] = 0
    while q:
        pos = q.pop()
        for st in path[pos]:
            if cost[st[0]] > cost[pos] + st[1]:
                q.appendleft(st[0])
                cost[st[0]] = cost[pos] + st[1]
                short[st[0]] = short[pos] + [pos]
    return cost[1]
'''


def get_shortest_path(short, c):
    q = deque()
    q.appendleft(N)
    cost = [math.inf for _ in range(N+1)]
    cost[N] = 0
    while q:
        pos = q.pop()
        for st in c[pos].keys():
            if cost[st] > cost[pos] + c[pos][st]:
                q.appendleft(st)
                cost[st] = cost[pos] + c[pos][st]
                short[st] = short[pos] + [pos]
    return cost[1]


q = deque()
conn = defaultdict(dict)
path = [[] for _ in range(N+1)]
short = [[] for _ in range(N+1)]

'''
for s, e, l in edges:
    path[s].append((e, l))
    path[e].append((s, l))
'''
for s, e, l in edges:
    if e not in conn[s]:
        conn[s][e] = l
        conn[e][s] = l

#_min = get_shortest_path(short, path)
_min = get_shortest_path(short, conn)

s = short[1]
pre = 1
sn = [[] for _ in range(N+1)]
sol = -1
for i in range(len(s)-1, -1, -1):
    org = conn[pre][s[i]]
    conn[pre][s[i]] = org*2
    conn[s[i]][pre] = org*2
    r = get_shortest_path(sn, conn) - _min
    sol = max(sol, r)
    conn[pre][s[i]] = org
    conn[s[i]][pre] = org
    pre = s[i]


# 출력하는 부분
print(sol)
