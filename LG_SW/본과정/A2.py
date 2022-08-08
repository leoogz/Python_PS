import sys


def Input_Data():
    readl = sys.stdin.readline
    N, P = map(int, readl().split())
    return N, P


sol = 0

# 입력받는 부분
N, P = Input_Data()

# 여기서부터 작성
d = {}

d[N] = 0
d[P] = 0

n = N
p = P

while True:
    n = N * n % P
    if n not in d:
        d[n] = 0
    elif d[n] == 0:
        d[n] += 1
    elif d[n] == 1:
        break

cnt = 0
for s in d.items():
    if s[1] == 1:
        cnt += 1
# 출력하는 부분
sol = cnt
print(sol)
