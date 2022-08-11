import sys


def Input_Data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input


sol = 0

# 입력받는 부분
str_input = Input_Data()

cnt = 0
fix = 0
# 여기서부터 작성
for n in str_input:
    if n == '(':
        cnt += 1
    else:
        if cnt > 0:
            cnt -= 1
        else:
            fix += 1
            cnt += 1
if cnt != 0:
    fix += cnt//2
# 출력하는 부분
sol = fix
print(sol)
