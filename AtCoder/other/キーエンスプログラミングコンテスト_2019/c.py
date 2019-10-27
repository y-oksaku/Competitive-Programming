N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [(a, b) for a, b in zip(A, B)]
AB.sort(key=lambda D: D[1] - D[0])

ans = 0
plus = 0
for a, b in AB[:: -1]:
    if a - b >= 0:
        break
    plus += b - a
    ans += 1

for a, b in AB:
    if a - b <= 0 or plus <= 0:
        break
    plus -= a - b
    ans += 1

if plus > 0:
    print(-1)
else:
    print(ans)

