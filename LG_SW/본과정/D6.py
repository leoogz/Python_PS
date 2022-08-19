import sys
from collections import defaultdict, deque


def Input_Data():
    readl = sys.stdin.readline
    P = int(readl())
    infos = [(lambda x:[x[0], x[1], int(x[2])])(readl().split())
             for _ in range(P)]
    return P, infos


sol_pos, sol_dist = -1, -1
# 입력받는 부분
P, infos = Input_Data()

# 여기서부터 작성
q = deque()
conn = defaultdict(dict)
cost = {}
cow = set()
for s, e, l in infos:
    if e in conn[s]:
        t = conn[s][e]
        if l < t:
            conn[s][e] = l
            conn[e][s] = l
    else:
        conn[s][e] = l
        conn[e][s] = l
    cost[s] = 99999
    cost[e] = 99999
    if s.isupper() and s != 'Z':
        cow.add(s)
    if e.isupper() and e != 'Z':
        cow.add(e)
q.appendleft('Z')
a = 0
cost['Z'] = 0
while q:
    pos = q.pop()
    for st in conn[pos]:
        if cost[st] > cost[pos] + conn[pos][st]:
            q.appendleft(st)
            cost[st] = cost[pos] + conn[pos][st]

a = 0
sol_pos = ''
sol_dist = 99999
for a in list(cow):
    if cost[a] < sol_dist:
        sol_pos = a
        sol_dist = cost[a]
# 출력하는 부분
print(sol_pos, sol_dist)
