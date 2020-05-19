N = int(input())
A = list(map(int, input().split()))

ans = 10**18
for a in range(min(A), max(A) + 1):
    cost = 0
    for b in A:
        cost += (a - b)**2
    ans = min(ans, cost)
print(ans)
