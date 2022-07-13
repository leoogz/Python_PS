import sys
from bisect import *
 
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query
 
 
sol = []
# 입력받는 부분
N, num, T, query = Input_Data()
 
def calCount(N,num,x):
    low = bisect_left(num,x,0,N)
    high = bisect_right(num,x,0,N)
    if high == low:
        if x == num[N] or x == num[1]:
            return 1
        else:
            return 0
    return high - low
# 여기서부터 작성
for i in range(T):
    sol.append(calCount(N,num,query[i]))
 
# 출력하는 부분
print(*sol)