import sys


def Input_Data():
    readl = sys.stdin.readline
    map_bingo = [list(map(int, readl().split())) for _ in range(5)]
    seq_bingo = []
    for _ in range(5):
        seq_bingo += list(map(int, readl().split()))
    return map_bingo, seq_bingo


sol = 0
# 입력받는 부분
map_bingo, seq_bingo = Input_Data()

# 여기서부터 작성
d_map = {}
row_s = [[] for _ in range(5)]
col_s = [[] for _ in range(5)]
diag_l = []
diag_r = []
Bingo = 0


def mark_map(r, c):
    global Bingo
    row_s[r].append(1)
    col_s[c].append(1)
    if r == c:
        diag_l.append(1)
        if len(diag_l) >= 5:
            Bingo += 1
    if r + c == 4:
        diag_r.append(1)
        if len(diag_r) >= 5:
            Bingo += 1


def find_bingo(r, c, cnt):
    global Bingo
    if cnt < 5:
        return
    else:
        if len(row_s[r]) >= 5:
            Bingo += 1
        if len(col_s[c]) >= 5:
            Bingo += 1


for i in range(5):
    for j in range(5):
        d_map[map_bingo[i][j]] = (i, j, 0)

cnt = 0
for s in seq_bingo:
    cnt += 1
    r = d_map[s][0]
    c = d_map[s][1]
    mark_map(r, c)
    find_bingo(r, c, cnt)
    if Bingo >= 3:
        break

sol = cnt
# 출력하는 부분

print(sol)
