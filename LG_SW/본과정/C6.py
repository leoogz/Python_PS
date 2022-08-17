import sys
from bisect import *


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_file = list(map(int, readl().split()))
    return N, list_file


sol = -1
# 입력받는 부분
N, list_file = Input_Data()

# 여기서부터 작성
cnt = 0
sol = 0
list_file.sort()


for i in range(N):
    p = bisect_left(list_file, 0.9 * list_file[i])
    cnt += i - p
sol = cnt
# 출력하는 부분
print(sol)
