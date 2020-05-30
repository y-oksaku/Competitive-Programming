N = int(input())
K = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += min(a * 2, (K - a) * 2)
print(ans)
