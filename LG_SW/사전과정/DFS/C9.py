import sys
from collections import *

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	return N, M


# 입력 받는 부분
N, M = Input_Data()
D = [0]*N


def dfs_1(s,n):
    if n == N:
        print(*D)
        return
    for i in range(1,7):   
        D[n] = i
        dfs_1(i,n+1)

def dfs_2(s,n):
    if n == N:
        print(*D)
        return
    for i in range(s,7):
        D[n] = i
        dfs_2(i,n+1)

def dfs_3(s,n):
    if n == N:
        print(*D)
        return
    for i in range(1,7):
        if i in D:
            continue
        D[n] = i
        dfs_3(i,n+1)
        D[n] = 0



if M == 1:
    dfs_1(1,0)
elif M == 2:
    dfs_2(1,0)
else:
    dfs_3(1,0)


# 여기서부터 작성