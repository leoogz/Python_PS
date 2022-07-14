import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[-1] + list(map(int, readl().strip())) + [-1] if 1<=r<=N else [-1] * (N+2) for r in range(N+2)]
	return N, map_uv


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
q = deque()
move = [(-1,0),(0,-1),(0,1),(1,0)]
map_his = [[9999] * (N+2) for n in range(N+2)]

t = map_his[1][1]
map_his[1][1] = 0
q.append((1,1))
while q:
    ch, cw = q.popleft()
    for n in move:
        nh = ch + n[0]
        nw = cw + n[1]
        if map_uv[nh][nw] < 0:
            continue
        if map_uv[nh][nw] + map_his[ch][cw] < map_his[nh][nw]:
            q.append((nh,nw))
            map_his[nh][nw] = map_uv[nh][nw] + map_his[ch][cw]


sol = map_his[N][N]
# 출력하는 부분
print(sol)