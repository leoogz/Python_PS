import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	M, N = map(int, readl().split())
	map_box = [[-1] + list(map(int, readl().split())) + [-1] if 1<=r<=N else [-1] * (M+2) for r in range(N+2)]
	return M, N, map_box


sol = -1
# 입력 받는 부분
M, N, map_box = Input_Data()

# 여기서부터 작성
move = [(0,1),(1,0),(0,-1),(-1,0)]
q = deque()
tomato_0 = 0
tomato_1 = 0
for i in range(1,N+1):
    for j in range(1, M+1):
        t = map_box[i][j]
        if t == 1:
            q.append((i,j))
            tomato_1 += 1
        elif t == 0:
            tomato_0 += 1
tomato_n = 0
if tomato_n == 0:
    while len(q) != 0:
        ch, cw = q.popleft()
        for d in move:
            nh, nw = d
            nh += ch
            nw += cw
            if map_box[nh][nw] == 0:
                map_box[nh][nw] = map_box[ch][cw] + 1
                q.append((nh,nw))
                tomato_n += 1
    if tomato_n == tomato_0:
        sol = map_box[ch][cw] - 1
    else:
        sol = -1
else:
    sol = 0
# 출력하는 부분
print(sol)