import sys


def input_data():
    readl = sys.stdin.readline
    N = int(input())
    return N


sol = 0

# 입력받는 부분
N = input_data()

# 여기서부터 작성
d = {}
d[10] = 1
n = 10


def prev_(n):
    x = 0
    while n >= 10:
        x += d[n]
        n = n//10
    return x


for i in range(1, 9):
    d[n*10] = d[n]*9 + n
    n *= 10


def cal_four(num, t):
    x = 0
    if num > 4:
        x += (num-1) * d[t] + t
    else:
        x += num * d[t]
    return x


def div_10(num):
    t = 10
    ans = 0
    while num > 10:
        num = num//10
        a = num % 10
        ans += cal_four(a, t)
        t *= 10
    return ans


t = N % 10
if t > 4:
    sol += 1
sol += div_10(N)

# 출력하는 부분
sol = N - sol
print(sol)
