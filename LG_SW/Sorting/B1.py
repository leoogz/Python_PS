import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = list(map(int, readl().split()))
	return N, num


# 입력받는 부분
N, num = Input_Data()

# 여기서부터 작성
num.sort()

# 출력하는 부분
print(*num)