N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

comb = [set() for _ in range(max(A) + max(B) + 1)]

for i, a in enumerate(A):
    for j, b in enumerate(B):
        if comb[a + b] and not (i, j) in comb[a + b]:
            for k, l in comb[a + b]:
                if i != k and j != l:
                    print(i, j, k, l)
                    exit()
        comb[a + b].add((i, j))

print(-1)

