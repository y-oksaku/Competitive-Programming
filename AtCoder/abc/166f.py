from itertools import combinations

N, A, B, C = map(int, input().split())
S = [input() for _ in range(N)]

def sol():
    now = {'A': A, 'B': B, 'C': C}
    ret = []
    for i, s in enumerate(S):
        u, v = s[0], s[1]
        if now[u] == now[v] == 0:
            return []
        if now[u] > now[v]:
            ret.append(v)
            now[u] -= 1
            now[v] += 1
            continue
        if now[u] < now[v]:
            ret.append(u)
            now[u] += 1
            now[v] -= 1
            continue
        if i == N - 1:
            ret.append(u)
            continue

        nx = S[i + 1]
        if u in nx:
            ret.append(u)
            now[u] += 1
            now[v] -= 1
            continue
        if v in nx:
            ret.append(v)
            now[v] += 1
            now[u] -= 1
            continue

    return ret

ans = sol()
if len(ans) == 0:
    print('No')
    exit()

print('Yes')
print(*ans, sep='\n')
