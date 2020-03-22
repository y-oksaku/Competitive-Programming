N = int(input())
A = list(map(int, input().split()))
T = 0
S = sum(A)

ans = 10**18
for a in A[:-1]:
    T += a
    S -= a
    ans = min(ans, abs(T - S))

print(ans)
