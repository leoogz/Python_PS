from struct import pack
import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    package = list(map(int,readl().split()))
    return N, package
 
 
sol = -1
# 입력받는 부분
N, package = Input_Data()
 
# 여기서부터 작성
sol = 0
for i in range(N-1):
    package[i:] = sorted(package[i:])
    package[i+1] = package[i] + package[i+1]
    sol += package[i+1]
     
# 출력하는 부분
 
print(sol)