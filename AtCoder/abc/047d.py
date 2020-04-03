N, T = map(int, input().split())
A = list(map(int, input().split()))

mi = 10**18
miCnt = 1
S = []
for i, a in enumerate(A):
    S.append((a - mi, i, miCnt))
    if a == mi:
        miCnt += 1
    elif a < mi:
        miCnt = 1
    mi = min(mi, a)

S.sort(reverse=True)
S = [c for v, i, c in S if v == S[0][0]]
ans = min(len(S), sum(S))
print(ans)
