N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort()
ans = AB[-1][0] + AB[-1][1]
print(ans)