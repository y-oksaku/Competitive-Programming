A, B, C = map(int, input().split())
ans = 0

if not (A % 2 == B % 2 == C % 2):
    G = [[], []]
    for n in (A, B, C):
        G[n % 2].append(n)
    G.sort(key=lambda a: len(a))

    G[1][0] += 1
    G[1][1] += 1

    A, B, C = G[0][0], G[1][0], G[1][1]
    ans += 1

mx = max(A, B, C)
ans += (mx - A) // 2 + (mx - B) // 2 + (mx - C) // 2
print(ans)
