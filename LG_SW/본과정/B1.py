import sys


def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    edges = [list(map(int, readl().split())) for _ in range(6)]
    return K, edges


sol = 0
# 입력받는 부분
K, edges = Input_Data()

# 여기서부터 작성

mx_a = 0
mx_b = 0
mx = 0
for i in range(5, -1, -1):
    t = edges[i][1] * edges[i-1][1]
    if t > mx:
        mx = t
        mx_a = i
        mx_b = i-1
mn_a = mx_a-3
mn_b = mx_b-3
mx = mx - (edges[mn_a][1] * edges[mn_b][1])
# 출력하는 부분
sol = K*mx
print(sol)
