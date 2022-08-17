import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    need = [int(readl()) for _ in range(N)]
    return N, M, need


sol = -1
# 입력 받는 부분
N, M, need = Input_Data()

# 여기서 부터 작성

start = max(need)
end = sum(need)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    res = 0
    for n in need:
        if res < n:
            cnt += 1
            res = mid
        res -= n

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        sol = mid

# 출력하는 부분
print(sol)
