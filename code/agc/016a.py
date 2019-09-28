S = input()

ans = float('inf')
for goal in S:
    dist = [float('inf')] * len(S)
    right = float('inf')
    for i in range(len(S))[:: -1]:
        if S[i] == goal:
            right = i
        dist[i] = min(dist[i], abs(i - right))

    cost = float('inf')
    for i in range(len(S)):
        cost = min(cost, max(i, max(dist[:len(S) - i])))
    ans = min(ans, cost)

print(ans)