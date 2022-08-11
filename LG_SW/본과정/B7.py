import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, input().split())) for _ in range(N)]
    return N, info


sol = -1
# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
info.sort(key=lambda x: x[1])

st = 0
et = 0
cmx = 0
c = 0
for i in range(N):
    s = info[i][0]
    e = info[i][1]
    if e - s < 2:
        continue
    if s >= et:
        st = s
        et = e
        c += 1

    if c > cmx:
        cmx = c
# 출력하는 부분
sol = cmx
print(sol)
