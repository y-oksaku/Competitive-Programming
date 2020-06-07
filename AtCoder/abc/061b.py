N, M = map(int, input().split())
ans = [0] * (N + 1)
for _ in range(M):
    fr, to = map(int, input().split())
    ans[fr] += 1
    ans[to] += 1

print(*ans[1:], sep='\n')
