import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    intvals = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, intvals


sol = -1
# 입력받는 부분
N, M, intvals = Input_Data()

# 여기서부터 작성


def check_distance(d):

    curr_p = -d
    cnt = 0
    for it in intvals:
        if (it[0] >= (curr_p + d)):
            cnt += 1
            curr_p = it[0]

        while (it[1] >= (curr_p + d)):
            cnt += 1
            curr_p += d

    if (cnt < N):
        return False
    return True


intvals.sort()
_min = 1
_max = intvals[-1][1]
prev = 0
mid = (_min + _max) // 2

while (prev != mid):

    ret = check_distance(mid)
    if (ret):
        _min = mid
    else:
        _max = mid
    prev = mid
    mid = (_min + _max) // 2

sol = mid
print(sol)
