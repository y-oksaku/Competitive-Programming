def sol():
    startX, startY, endX, endY, T, V = map(int, input().split())
    N = int(input())
    girls = []
    for _ in range(N):
        a, b = map(int, input().split())
        girls.append((a, b))

    def dist(a, b, x, y):
        return ((a - x)**2 + (b - y)**2)**0.5


    for a, b in girls:
        if dist(startX, startY, a, b) + dist(a, b, endX, endY) <= T * V:
            print('YES')
            return
    print('NO')


sol()