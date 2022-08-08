import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


sol = 0
# 입력받는 부분
N = Input_Data()

D = {}
# 여기서부터 작성


def happy(d, n):
    while True:
        if n == 1:
            return True
        if n not in d:
            d[n] = 1
        elif d[n] == 1:
            return False
        mstr = str(n)
        t = 0
        for s in mstr:
            a = int(s)
            t += a * a
        n = t


# 출력하는 부분
for i in range(N):
    D = {}
    h = happy(D, N-i)
    if h:
        sol = N-i
        break
print(sol)
