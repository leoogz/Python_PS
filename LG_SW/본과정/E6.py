import sys


def input_data():
    A, N = map(int, readl().split())
    W = list(map(int, readl().split()))
    return A, N, W


readl = sys.stdin.readline
T = int(readl())
for t in range(1, T+1):
    # 입력받는 부분
    A, N, W = input_data()
    _max = 9999999
    # 여기서부터 작성

    def dfs(a, i, cnt):
        global _max
        if i >= N:
            _max = min(_max, cnt)
            return
        if W[i] >= 2*a - 1:
            dfs(a, i+1, cnt+1)
            t = 0
            if a > 1:
                while a <= W[i]:
                    t += 1
                    a += a - 1
                dfs(a + W[i], i+1, cnt+t)
        elif W[i] >= a:
            dfs(a + a-1 + W[i], i+1, cnt + 1)
        else:
            dfs(a + W[i], i+1, cnt)

        return

    def Solve():
        a = A
        W.sort()
        cnt = 0
        dfs(a, 0, 0)
        return _max

    sol = Solve()
    print('Case #{0}: {1}'.format(t, sol))
