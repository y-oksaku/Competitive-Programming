D = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
now = 0
ans = float('inf')
for a, b in zip(A, B):
    now += a
    if b <= now:
        ans = min(ans, b)

print(ans if ans != float('inf') else -1)