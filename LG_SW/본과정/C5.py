import sys
import copy


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = 0

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성

_min = min(info, key=lambda x: x[1])[1]
_max = max(info, key=lambda x: x[1])[1]


def spread_fish(ref):

    remain_fish = 0
    gap_cost = 0

    t_data = copy.deepcopy(info)

    for idx in range(N):

        if (remain_fish > gap_cost):
            remain_fish -= gap_cost
        else:
            remain_fish = 0

        diff = t_data[idx][1] - ref

        remain_fish += diff

        if (idx >= (N - 1)):
            break

        gap_cost = (t_data[idx+1][0] - t_data[idx][0])

        if (remain_fish < 0):
            t_data[idx+1][1] += (remain_fish - gap_cost)
            remain_fish = 0

    return remain_fish


prev_mid = 0

while (1):
    mid = (_min + _max) // 2

    remain = spread_fish(mid)

    if (remain > 0):
        min_val = mid

    elif (remain < 0):
        _max = mid

    if (sol == mid):
        break
    sol = mid


# 출력하는 부분
print(sol)
