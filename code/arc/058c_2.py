N, K = map(int, input().split())
D = set(input().split())

safe = set([str(i) for i in range(10) if not str(i) in D])

ans = N
while not all([i in safe for i in str(ans)]):
    ans += 1

print(ans)
