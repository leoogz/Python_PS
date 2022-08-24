import sys


def input_data():
    map_soli = [[0] + list(readl().strip()) + [0] if 1 <=
                r <= 5 else [0]*11 for r in range(7)]
    readl()
    return map_soli


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    map_soli = input_data()
    # 여기서부터 작성
    _minP = 999999
    _minM = 999999
    dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    def dfs(r, c, pN, move):
        global _minP
        global _minM

        if pN == _minP:
            _minM = min(_minM, move)
        elif pN < _minP:
            _minP = pN
            _minM = move

        for d in dir:
            nr = r + d[0]
            nc = c + d[1]

            if map_soli[nr][nc] != 'o':
                continue

            nnr = nr + d[0]
            nnc = nc + d[1]
            if map_soli[nnr][nnc] == '.':
                map_soli[r][c] = '.'
                map_soli[nr][nc] = '.'
                map_soli[nnr][nnc] = 'o'
                for i in range(1, 5):
                    for j in range(1, 10):
                        if map_soli[i][j] == 'o':
                            dfs(i, j, pN-1, move+1)
                map_soli[r][c] = 'o'
                map_soli[nr][nc] = 'o'
                map_soli[nnr][nnc] = '.'
        return

    def Solve():
        pN = 0
        pin = []
        for i in range(1, 6):
            for j in range(1, 10):
                if map_soli[i][j] == 'o':
                    pN += 1
                    pin.append((i, j))

        for i, j in pin:
            dfs(i, j, pN, 0)
        return

    Solve()
    print(_minP, _minM)
