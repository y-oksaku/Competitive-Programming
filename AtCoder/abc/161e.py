N, K, C = map(int, input().split())
S = input()

def calc(S):
    now = 1
    ret = [0] * (N + 1)
    while now <= N:
        if S[now] == 'x':
            now += 1
            continue
        ret[now] += 1
        now += C + 1
    for i in range(N):
        ret[i + 1] += ret[i]

    return ret

L = calc('-' + S)
R = calc('-' + S[::-1])[::-1]

ans = []
for mid in range(1, N + 1):
    if S[mid - 1] == 'o' and L[mid] != L[mid - 1] and R[mid] != R[mid - 1] and L[mid] + R[mid] == K:
        ans.append(mid)

print(*ans, sep='\n')