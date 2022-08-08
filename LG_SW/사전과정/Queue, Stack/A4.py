from re import A
import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int,str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op
 
 
sol = -1
# 입력받는 부분
N, nums, op = Input_Data()
 
# 여기서부터 작성
nums = deque(nums)
op = deque(op)
flag = 1
tmp = nums.popleft()
sol = 0
while op:
    p = op.popleft()
    if p == '+' or p == '-':
        sol += flag * tmp
        if p == '-':
            flag = -1
        else:
            flag = 1
        tmp = nums.popleft()
    elif p == '*':
        tmp = tmp * nums.popleft()
    else:
        tmp = int(tmp/nums.popleft())
# 출력하는 부분
sol += tmp * flag
print(sol)