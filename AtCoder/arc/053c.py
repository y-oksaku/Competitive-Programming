N = int(input())

plus = []
minus = []
zero = []
now = 0

for _ in range(N):
    A, B = map(int, input().split())
    now += A - B
    if A - B < 0:
        minus.append((A, B))
    elif A - B > 0:
        plus.append((A, B))
    else:
        zero.append((A, B))

ans = now
plus.sort(key=lambda C: C[1])
for a, b in plus:
    now += b
    ans = max(ans, now)
    now -= a

for a, b in zero:
    now += b
    ans = max(ans, now)
    now -= a

now = 0
minus.sort(key=lambda C: C[0])
for a, b in minus:
    now += a
    ans = max(ans, now)
    now -= b

print(ans)