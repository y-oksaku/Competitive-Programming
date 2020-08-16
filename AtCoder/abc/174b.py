N, D = map(int, input().split())

ans = 0
D2 = D**2

for _ in range(N):
    X2, Y2 = map(lambda a: int(a)**2, input().split())
    if X2 + Y2 <= D2:
        ans += 1
print(ans)
