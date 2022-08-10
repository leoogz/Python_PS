import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num


sol = 0.0
# 입력받는 부분
N, num = Input_Data()

# 여기서부터 작성
mx = 0
x = num[0]
for i in range(1, N):
    t = x * num[i]
    a = num[i]
    if t < num[i]:
        x = num[i]
    else:
        x = t
    if mx < x:
        mx = x
# 출력하는 부분
sol = mx
print(f"{sol:.3f}")
