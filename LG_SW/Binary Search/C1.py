import sys
from bisect import *
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = list(map(int, readl().split()))
    M = int(readl())
    return N, pos, M
 
 
sol = -1
# 입력받는 부분
N, pos, M = Input_Data()
 
# 여기서부터 작성
def check_sum(x):
    s = 0
    for i in pos:
        s += i if i < x else x
    return s <= M
 
def solve(N,pos,M):
    pos.sort()
    s, e = 0, pos[N-1]
    ret = 0
    while s <= e:
        m = int((s+e)/2)
        if check_sum(m):
            s = m + 1
            ret = m
        else:
            e = m - 1
    return ret
 
 
 
# 출력하는 부분
sol = solve(N,pos,M)
print(sol)