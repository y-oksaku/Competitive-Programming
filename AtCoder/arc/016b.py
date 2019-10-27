N = int(input())

A = [['.' for _ in range(9)]] + [list(input()) for _ in range(N)]

ans = 0
for time in range(1, N + 1):
    for button in range(9):
        if A[time][button] == 'x':
            ans += 1
        if A[time][button] == 'o' and A[time - 1][button] != 'o':
            ans += 1

print(ans)