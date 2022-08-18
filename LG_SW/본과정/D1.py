import sys
import math
from collections import deque, defaultdict


def Input_Data():
    readl = sys.stdin.readline
    S, E = map(int, readl().split())
    return S, E


sol = -2

# 입력받는 부분
S, E = Input_Data()

# 여기서부터 작성
p = {}
a = '0123456789'


def find_prime():

    for x in range(2, 10000):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                break
        else:
            p[str(x)] = True


def is_prime(x):
    if x in p:
        return True
    return False


def Solve(S, E):
    check = defaultdict(int)
    cnt = 0
    stk = deque()
    stk.appendleft(S)
    check[S] = 1
    while len(stk):
        s = stk.pop()
        cnt = check[s]
        for i in range(4):
            for j in a:
                t = s[:i] + j + s[i+1:]
                if t == E:
                    return cnt
                if is_prime(t) and check[t] == 0:
                    stk.appendleft(t)
                    check[t] = check[s] + 1

    return cnt


find_prime()
sol = Solve(str(S), str(E))
# 출력하는 부분
print(sol)
