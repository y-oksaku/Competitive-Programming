N, K = map(int, input().split())

edges = [(1, to) for to in range(2, N + 1)]
M = (N - 1) * (N - 2) // 2

if K > M:
    print(-1)
    exit()

for fr in range(2, N + 1):
    for to in range(fr + 1, N + 1):
        if M == K:
            break
        edges.append((fr, to))
        M -= 1

print(len(edges))
for fr ,to in edges:
    print(fr ,to)
