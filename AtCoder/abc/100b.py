D, N = map(int, input().split())

ans = pow(100, D)

if N < 100:
    ans *= N
else:
    ans *= 101

print(ans)
