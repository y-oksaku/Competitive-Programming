N = int(input())
Q = int(input())

R = [N * i for i in range(N)]
C = list(range(N))

def get(i, j):
    return R[i] + C[j]

ans = []

for _ in range(Q):
    query = tuple(map(lambda a: int(a) - 1, input().split()))

    if query[0] == 0:
        x, y = query[1:]
        R[x], R[y] = R[y], R[x]

    if query[0] == 1:
        x, y = query[1:]
        C[x], C[y] = C[y], C[x]

    if query[0] == 2:
        R, C = C, R

    if query[0] == 3:
        i, j = query[1:]
        ans.append(get(i, j))

print(*ans, sep='\n')
