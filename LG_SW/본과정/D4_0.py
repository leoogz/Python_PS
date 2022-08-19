import sys
import math
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int, readl().split())) +
                    [0] if 1 <= r <= N else [0] * (N+2) for r in range(N+2)]
    return N, r_top, c_top, map_mountine


def BFS():
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    chk = [[math.inf] * (N+2) for _ in range(N+2)]  # 각 위치 별 최고의 경험

    # 출발 가능 위치 모두 초기상태로 정의
    for n in range(1, N+1):
        q.append((0, n, 0))
        chk[0][n] = 0
        q.append((N+1, n, 0))
        chk[N+1][n] = 0
        q.append((n, 0, 0))
        chk[n][0] = 0
        q.append((n, N+1, 0))
        chk[n][N+1] = 0

    '''  
    # 출발 가능 위치 중 한 위치만 초기상태로 정의
    q.append((0, 0, 0))
    chk[0][0] = 0   
    '''

    while q:
        r, c, sum_power = q.popleft()
        if chk[r][c] < sum_power:
            continue
        for dr, dc in d:
            nr, nc = r+dr, c+dc

            if not 0 <= nr <= N+1:
                continue                       # 좌표 유효성 판단
            if not 0 <= nc <= N+1:
                continue
            diff = map_mountine[r][c] - \
                map_mountine[nr][nc]    # 다음 위치와의 높이 관계 확인
            if diff < 0:
                nsum_power = sum_power + diff**2       # diff -> 음수 ?  오르막 이동
            else:
                nsum_power = sum_power + diff                 # 아니라면 평지 혹은 내리막 이동

            if chk[nr][nc] <= nsum_power:
                continue               # 다음상태 최고의 경험보다 좋지 않다면? 경우의 수 차단!
            chk[nr][nc] = nsum_power                            # 다음 상태 발전 결정!
            q.append((nr, nc, nsum_power))

    return chk[r_top][c_top]  # 목표지 최고의 경험 리턴


sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)
