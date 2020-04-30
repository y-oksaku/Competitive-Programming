H, W, K = map(int, input().split())

S = [input() for _ in range(H)]

def calc(L):
    M = len(L)
    cnt = [0] * M
    ret = 0

    for w in range(W):
        for i, (t, b) in enumerate(zip(L, L[1:])):
            for j in range(t, b):
                if S[j][w] == '1':
                    cnt[i] += 1
        if max(cnt) > K:
            cnt = [0] * M
            ret += 1
            for i, (t, b) in enumerate(zip(L, L[1:])):
                for j in range(t, b):
                    if S[j][w] == '1':
                        cnt[i] += 1
        if max(cnt) > K:
            return 10**18

    return ret

ans = 10**18
for mask in range(1 << (H - 1)):
    L = [0] + [d + 1 for d in range(H - 1) if (mask & (1 << d)) > 0] + [H]
    ans = min(ans, len(L) - 2 + calc(L))
print(ans)
