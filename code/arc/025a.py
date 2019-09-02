D = list(map(int, input().split()))
L = list(map(int, input().split()))

ans = 0
for d, l in zip(D, L):
    ans += max(d, l)
print(ans)