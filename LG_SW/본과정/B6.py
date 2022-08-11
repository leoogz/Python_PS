import sys


def Input_Data():
    N = int(sys.stdin.readline())
    list_time = [list(map(int, sys.stdin.readline().split()))
                 for _ in range(N)]
    return N, list_time


sol = [-1, -1]
# 입력받는 부분
N, list_time = Input_Data()

# 여기서부터 작성
list_time.sort(key=lambda x: x[0])

st = list_time[0][0]
et = list_time[0][1]
em = 0
sm = 0
for i in range(1, N):
    if list_time[i][0] <= et and list_time[i][1] > et:
        et = list_time[i][1]
    elif et < list_time[i][0]:
        t = list_time[i][0] - et
        s = et - st
        if s > sm:
            sm = s
        if t > em:
            em = t
        et = list_time[i][1]
        st = list_time[i][0]
s = et - st
if s > sm:
    sm = s
# 출력하는 부분
sol[0] = sm
sol[1] = em
print(*sol)
