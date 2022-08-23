import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight


sol = -1
# 입력받는 부분
N, weight = input_data()
_max = 0
# 여기서부터 작성


def on_board(prev, next):
    while prev > 0 or next > 0:
        p = prev % 10
        n = next % 10
        if p + n >= 10:
            return False
        prev = prev // 10
        next = next // 10
    return True


def boat(sum, i, cnt):
    global _max
    _max = max(_max, cnt)
    if i >= N:
        return

    next = weight[i]
    if on_board(sum, next):
        boat(sum + next, i+1, cnt + 1)
    boat(sum, i+1, cnt)
    return


def Solve():
    ret = 0
    boat(0, 0, 0)
    ret = _max
    return ret
# 출력하는 부분


sol = Solve()
print(sol)
