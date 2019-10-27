N, A, B, C = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))

ans = float('inf')
for mask in range(pow(4, N)):
    cost = 0
    for i, l in enumerate([A, B, C]):
        grp = []
        for digit in range(N):
            if mask // pow(4, digit) % 4 == i:
                grp.append(L[digit])

        if not grp:
            cost = float('inf')

        cost += (len(grp) - 1) * 10
        cost += abs(l - sum(grp))
    ans = min(ans, cost)

print(ans)