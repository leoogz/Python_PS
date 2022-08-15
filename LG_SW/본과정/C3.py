import sys
from collections import deque


def Input_data():
    readl = sys.stdin.readline
    N, *list_height = map(int, readl().split())
    return N, list_height


sol = []


def Solve(N, list_height):
    stk = deque()
    i = 0
    _max = 0
    for i in range(N):
        while len(stk) != 0 and list_height[stk[-1]] > list_height[i]:
            tmp = stk.pop()

            if len(stk) == 0:
                width = i
            else:
                width = i - stk[-1] - 1
            _max = max(_max, width * list_height[tmp])
        stk.append(i)

    # 스택에 남아있는 것을 처리
    while len(stk) != 0:
        tmp = stk.pop()

        if len(stk) == 0:
            width = N
        else:
            width = N - stk[-1] - 1
        _max = max(_max, width * list_height[tmp])

    print(_max)


while 1:
    # 입력받는 부분
    N, list_height = Input_data()
    if N == 0:
        break
    Solve(N, list_height)
