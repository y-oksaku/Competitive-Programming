X, N = map(int, input().split())
P = set(map(int, input().split()))

ans = 10**18

for i in range(-100, 200):
    if i in P:
        continue
    if abs(X - i) < abs(X - ans):
        ans = i
    if abs(X - i) == abs(X - ans):
        if i < ans:
            ans = i

print(ans)
