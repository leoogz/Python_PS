import sys


def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    N = int(readl())
    info = [readl().split() for _ in range(N)]
    info = [(int(t), z) for t, z in info]
    return K, N, info


# 입력받는 부분
K, N, info = Input_Data()
sol = 0

# 여기서부터 작성


def bomb():
    p = K
    cur_t = 0
    expl_t = 210
    clear = 0
    for s in info:
        if clear >= N:
            return p
        cur_t += s[0]
        if cur_t > 210:
            return p

        if s[1] == 'T':
            p += 1
            clear += 1
            continue
        else:
            continue

    return p


sol = bomb() % 8
if sol == 0:
    sol = 8

# 출력하는 부분
print(sol)
