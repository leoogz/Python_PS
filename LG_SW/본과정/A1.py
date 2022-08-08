import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [int(readl()) for _ in range(N)]
    return N, num


sol = 0

# 입력받는 부분
N, num = Input_Data()


# 여기서부터 작성
max = 0


def num_root(n):
    while n//10 > 0:
        mstr = str(n)
        t = 0
        for i in range(len(mstr)):
            t += int(mstr[i])
        n = t
    return n


for i in range(N):
    n = num[i]
    t = num_root(n)
    if max < t:
        max = t
        sol = i
    elif max == t:
        if num[sol] > num[i]:
            sol = i

# 출력하는 부분
sol = num[sol]
print(sol)
