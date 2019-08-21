N = int(input())
A = list(map(int, input().split()))

ans = float('inf')

for base in range(min(A), max(A) + 1):
    ans = min(ans, sum([abs(base - a)**2 for a in A]))

print(ans)