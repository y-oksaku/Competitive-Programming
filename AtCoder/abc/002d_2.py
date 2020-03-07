N, M = map(int, input().split())
S = set([tuple(map(lambda a: int(a) - 1, input().split())) for _ in range(M)])

def canMake(I):
    for i in I:
        for j in I:
            if i == j:
                continue
            if not ((i, j) in S or (j, i) in S):
                return False
    return True

ans = 0
for state in range(1 << N):
    I = [i for i in range(N) if (state & (1 << i)) > 0]
    if canMake(I):
        ans = max(ans, len(I))

print(ans)