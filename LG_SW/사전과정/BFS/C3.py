import sys
from collections import *
def Input_Data():
	readl = sys.stdin.readline
	W, H = map(int, readl().split())
	sw, sh, ew, eh = map(int, readl().split())
	map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
	return W, H, sw, sh, ew, eh, map_maze


sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
q = deque()
dir = [(-1,0), (0,-1) , (1, 0), (0, 1)]
visit = [[1] + [0]*W + [1] if 1<=h<=H else [1] * (W+2) for h in range(H+2)]
q.append((sh,sw))
visit[sh][sw] += 1
time = 0
while len(q) != 0:
	ch, cw = q.popleft()
	if (cw, ch) == 	(ew, eh):
		break
	for i in range(4):
		th, tw = ch+dir[i][0], cw+dir[i][1]
		if map_maze[th][tw] == 0 and visit[th][tw] == 0:
			q.append((th,tw))
			visit[th][tw] = visit[ch][cw] + 1
			
sol = visit[eh][ew] - 1


# 출력하는 부분
print(sol)