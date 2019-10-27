N = int(input())
trains = []
for _ in range(N - 1):
    c, s, f = map(int, input().split())
    trains.append((c, s, f))

for start in range(0, N):
    now = 0
    for c, s, f in trains[start:]:
        if now < s:
            now = s
        now += (f - now % f) % f
        now += c
    print(now)
