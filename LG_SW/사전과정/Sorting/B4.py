import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_score = list(map(int, readl().split()))
    return N, list_score
 
 
sol = [-1, -1, -1]
# 입력받는 부분
N, list_score = Input_Data()
 
# 여기서부터 받는
for i in range(N):
    list_score[i] = (list_score[i],i+1)
list_score.sort(reverse=True,key = lambda x: (x[0],-x[1]))
for i in range(0,3):
    sol[i] = list_score[i][1]
 
# 출력하는 부분
print(*sol)