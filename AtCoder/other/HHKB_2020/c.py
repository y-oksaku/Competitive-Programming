N = int(input())
P = list(map(int, input().split()))

ans = []
mi = 0
V = set()
for p in P:
    V.add(p)
    while mi in V:
        mi += 1
    ans.append(mi)
print(*ans, sep='\n')
