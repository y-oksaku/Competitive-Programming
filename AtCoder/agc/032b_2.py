N = int(input())

V = set()

if N % 2 == 0:
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i + j == N + 1:
                V.add((i, j))
else:
    for i in range(1, N):
        for j in range(i + 1, N):
            if i + j == N:
                V.add((i, j))

ans = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if not (i, j) in V:
            ans.append((i, j))

print(len(ans))
for a in ans:
    print(*a)
