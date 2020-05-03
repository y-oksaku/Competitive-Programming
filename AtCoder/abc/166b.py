N, K = map(int, input().split())
cnt = [0] * N
for _ in range(K):
    _ = int(input())
    for a in map(int, input().split()):
        cnt[a - 1] += 1

print(cnt.count(0))

