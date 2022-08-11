import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = 0

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
paper = [[0 for _ in range(102)] for _ in range(102)]
# 출력하는 부분

cnt = 0

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for n in info:
    x = n[0]
    y = n[1]
    for i in range(10):
        for j in range(10):
            if paper[y+i][x+j] == 0:
                paper[y+i][x+j] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            for d in D:
                if paper[i+d[0]][j+d[1]] == 0:
                    cnt += 1

sol = cnt
print(sol)
