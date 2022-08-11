import sys


def Input_Data():
    N = int(sys.stdin.readline())
    list_meeting = [list(map(int, sys.stdin.readline().split()))
                    for _ in range(N)]
    return N, list_meeting


# 입력받는 부분
N, list_meeting = Input_Data()

# 여기서부터 작성
list_meeting.sort(key=lambda x: x[2])

etime = 0
result = []
for n in list_meeting:
    if n[1] >= etime:
        etime = n[2]
        result.append(n[0])
# 출력하는 부분
print(len(result))
print(*result)
