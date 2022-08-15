import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    M, T, N = map(int, readl().split())
    info = [list(readl().split()) for _ in range(N)]
    info = [[i, int(s[0]), s[1]] for i, s in enumerate(info)]
    return M, T, N, info


def Passanger_At_Stop(cur, stop, idx):
    while idx < N and info[idx][1] <= cur:
        side = info[idx][2] == "right"
        stop[side].append(info[idx][0])
        idx += 1
    return idx


def Get_On_A_Ship(ship, stop, ship_side):
    while len(ship) < M and stop[ship_side]:
        ship.append(stop[ship_side].popleft())


def Passanger_Arrived_At_Dest(cur, ret, ship, cnt_arrived):
    while ship:
        ret[ship.popleft()] = cur
        cnt_arrived += 1

    return cnt_arrived


def Solve():
    ret = [0] * N
    ship_side = 0
    ship = deque()
    stop = [deque(), deque()]
    info.sort(key=lambda x: (x[1], x[0]))
    cnt_arrived = 0
    cur = 0
    idx = 0

    while cnt_arrived < N:
        idx = Passanger_At_Stop(cur, stop, idx)
        Get_On_A_Ship(ship, stop, ship_side)

        if len(ship) == 0 and len(stop[0]) == 0 and len(stop[1]) == 0 and idx < N:
            cur = info[idx][1]
            idx = Passanger_At_Stop(cur, stop, idx)
            Get_On_A_Ship(ship, stop, ship_side)

        ship_side = 0 if ship_side else 1  # ship_side ^ 1
        cur += T

        cnt_arrived = Passanger_Arrived_At_Dest(cur, ret, ship, cnt_arrived)
    return ret


M, T, N, info = Input_Data()
ret = Solve()
print(*ret, sep='\n')
