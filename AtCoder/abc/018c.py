R, C, K = map(int, input().split())
S = [list(input()) for _ in range(R)]

countTop = [[0 for _ in range(C)] for _ in range(R)]
countBottom = [[0 for _ in range(C)] for _ in range(R)]

for c in range(C):
    top = 0
    bottom = 0
    for r in range(R):
        countTop[r][c] = top
        if S[r][c] == 'o':
            top += 1
        else:
            top = 0

        countBottom[-1 - r][c] = bottom
        if S[-1 - r][c] == 'o':
            bottom += 1
        else:
            bottom = 0

ans = 0
for r in range(K - 1, R - K + 1):
    for c in range(K - 1, C - K + 1):
        for k in range(-K + 1, K):
            if S[r][c + k] == 'x':
                break
            if countTop[r][c + k] < K - 1 - abs(k) or countBottom[r][c + k] < K - 1 - abs(k):
                break
        else:
            ans += 1

print(ans)