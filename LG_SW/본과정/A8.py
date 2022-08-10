import sys


def Input_Data():
    read = sys.stdin.readline
    N, d, k, c = map(int, read().split())
    dish = [int(read()) for _ in range(N)]
    return N, d, k, c, dish


sol = 0
# 입력받는 부분
N, d, k, c, dish = Input_Data()

# 여기서부터 작성
mx = 0
D = {}
D[c] = 300000
for j in range(0, k):
    t = dish[N-j-1]
    if t not in D:
        D[t] = 1
    else:
        D[t] += 1
mx = len(D)
for i in range(N-1, -1, -1):
    if D[dish[i]] == 1:
        D.pop(dish[i])
    else:
        D[dish[i]] -= 1
    t = dish[i-k]
    if t not in D:
        D[t] = 1
    else:
        D[t] += 1
    if len(D) > mx:
        mx = len(D)

# 출력하는 부분
sol = mx
print(sol)
