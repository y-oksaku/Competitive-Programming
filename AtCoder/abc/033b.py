N = int(input())
SP = [input().split() for _ in range(N)]
M = sum(map(int, (p for _, p in SP)))

ans = list(filter(lambda a: int(a[1]) * 2 > M, SP))
print(ans[0][0] if ans else 'atcoder')
