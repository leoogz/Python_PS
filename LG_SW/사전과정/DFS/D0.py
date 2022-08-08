import sys

def Input_Data():
	N, K = map(int, readl().split())
	num = list(map(int, readl().split()))
	return N, K, num

sol = []
# 입력 받는 부분
readl = sys.stdin.readline



T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
	# 여기서부터 입력
    def plus(n,sum):
        if sum > K:
            return False
        elif sum == K:
            return True
        for i in range(n,N):
            if plus(i+1,sum + num[i]):
                return True
        return False

    def Solve(N,K,num):
        ret = 'NO'
        if plus(0,0):
            ret = "YES"

        return ret
    sol.append(Solve(N,K,num))


# 출력하는 부분
print(*sol, sep = '\n')