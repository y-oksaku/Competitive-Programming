N = int(input())

ans = set()
for i in range(1, int(N**0.5) + 100):
    if N % i == 0:
        ans.add(i)
        ans.add(N // i)
ans = list(ans)
ans.sort()

print(*ans, sep='\n')
