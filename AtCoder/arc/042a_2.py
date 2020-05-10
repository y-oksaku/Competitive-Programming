N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

ans = []
V = set()
for a in A[::-1]:
    if not a in V:
        ans.append(a)
        V.add(a)

for i in range(1, N + 1):
    if not i in V:
        ans.append(i)

print(*ans, sep='\n')

