import sys


def Input_Data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    N, B, height = Input_Data()
    # 여기서부터 작성

    def cal_height(i, book, _min):
        b = list(book)
        for a in b:
            t = a + height[i]
            if t >= B:
                _min = min(_min, t)
            book.add(t)
        book.add(height[i])
        return _min

    def Solve():
        book = set()
        _min = 99999999999
        for i in range(N):
            _min = cal_height(i, book, _min)

        return _min

    sol = Solve() - B
    print(sol)
