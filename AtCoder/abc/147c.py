N = int(input())

M = []
for _ in range(N):
    A = int(input())
    state = []
    for _ in range(A):
        x, y = map(int, input().split())
        x -= 1
        state.append((x, y))
    M.append(state)

ans = 0
for mask in range(1 << N):
    can = True
    for i, s in enumerate(M):
        if (mask & (1 << i)) != 0:
            for x, y in s:
                v = 1 if (mask & (1 << x)) != 0 else 0
                if v != y:
                    can = False
                    break
    if can:
        cnt = 0
        for i in range(N):
            if (mask & (1 << i)) != 0:
                cnt += 1
        ans = max(ans, cnt)

print(ans)