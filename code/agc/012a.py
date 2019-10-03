N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
for a in A[N:: 2]:
    ans += a

print(ans)