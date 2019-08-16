N = int(input())
S = [list(input()) for _ in range(N)] + [['o' for _ in range(N)]] + [['o' for _ in range(N)]]

ans = 0
row = 0
while row <= N:
    right = -1
    left = float('inf')
    for i, (sa, sb) in enumerate(zip(S[row], S[row + 1])):
        if sa == '.':
            right = i
        if sb == '.':
            left = min(left, i)

    if right == -1 and left == float('inf'):
        row += 2
        continue

    if right <= left:
        ans += 1
        row += 2
    else:
        for j in range(right, N):
            S[row + 1][j] = 'o'
        ans += 1
        row += 1

print(ans)
