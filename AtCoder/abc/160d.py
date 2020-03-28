N, X, Y = map(int, input().split())

def dist(fr, to):
    return min(
        to - fr,
        abs(to - Y) + 1 + abs(fr - X),
        abs(fr - Y) + 1 + abs(to - X)
    )

cnt = [0] * N

ans = 0
for fr in range(1, N + 1):
    for to in range(fr + 1, N + 1):
        cnt[dist(fr, to)] += 1

print(*(cnt[1:]), sep='\n')