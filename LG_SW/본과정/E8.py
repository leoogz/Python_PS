import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    W = int(readl())
    pos = [list(map(int, readl().split())) for n in range(W)]
    return N, W, pos


sol = -1
# 입력받는 부분
N, W, pos = Input_Data()
_min = 9999999
# 여기서부터 작성


def cal_dis(rc, p):

    return abs(p[0] - rc[0]) + abs(p[1] - rc[1])


def DFS(rc, i, dis):
    global _min
    if i >= W:
        _min = min(_min, dis)
        return
    nrc = [pos[i], rc[1]]
    DFS(nrc, i+1, dis + cal_dis(rc[0], pos[i]))
    nrc = [rc[0], pos[i]]
    DFS(nrc, i+1, dis + cal_dis(rc[1], pos[i]))
    return


def Solve():
    rc = [[1, 1], [N, N]]
    DFS(rc, 0, 0)

    return _min


sol = Solve()
# 출력하는 부분
print(sol)
