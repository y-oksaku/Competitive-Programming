N = int(input())
S = input()

AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

light = [int(s) for s in S]
ans = sum(light)
for t in range(1, 1001):
    ans = max(ans, sum(light))
    for i, (a, b) in enumerate(AB):
        if t >= b and (t - b) % a == 0:
            light[i] = 1 if light[i] == 0 else 0

print(ans)