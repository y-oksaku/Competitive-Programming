N, K = map(int, input().split())
count = [0 for _ in range(10**5 + 100)]

for _ in range(N):
    a, b = map(int, input().split())
    count[a] += b

now = 0
ans = 0
for i, c in enumerate(count):
    now += c
    if now >= K:
        ans = i
        break

print(ans)