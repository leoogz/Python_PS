import sys
 
 
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
 
# 여기서부터 작성
 
def bi_search(N,num,key):
    low = 1
    high = N
     
    while low <= high:
        mid = int((high + low)/2)
        if key == num[mid]:
            return mid
        elif key < num[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0
         
 
 
for i in range(T):
    sol.append(bi_search(N,num,query[i]))
 
# 출력하는 부분
print(*sol, sep = '\n')