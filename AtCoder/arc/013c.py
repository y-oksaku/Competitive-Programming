import sys
input = sys.stdin.buffer.readline

N = int(input())
INF = 10**18
nim = 0

for _ in range(N):
    X, Y, Z = map(int, input().split())
    M = int(input())
    mi = [INF] * 3
    mx = [-1] * 3

    for _ in range(M):
        for i, a in enumerate(map(int, input().split())):
            mi[i] = min(mi[i], a)
            mx[i] = max(mx[i], a)

    mx[0] = X - mx[0] - 1
    mx[1] = Y - mx[1] - 1
    mx[2] = Z - mx[2] - 1

    for c in mi:
        nim ^= c
    for c in mx:
        nim ^= c

print('WIN' if nim > 0 else 'LOSE')
