import sys
from collections import defaultdict


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    words = readl().split()
    return N, words


# 입력받는 부분
N, words = Input_Data()

# 여기서부터 작성
D = {}
for i in range(N):
    if words[i] not in D:
        D[words[i]] = []
    D[words[i]].append(i+1)

flag = 0
for d in D.items():
    if len(d[1]) != 1:
        flag = 1
        print(d[0], end='')
        for n in d[1]:
            print('', n, end='')
        print()
if flag == 0:
    print('unique')
# 출력하는 부분
