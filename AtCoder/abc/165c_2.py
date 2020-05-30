N, M, Q = map(int, input().split())
ABCD = [tuple(map(int, input().split())) for _ in range(Q)]

X = []
ans = 0

def calc():
    ret = 0
    for a, b, c, d in ABCD:
        if X[b - 1] - X[a - 1] == c:
            ret += d
    return ret

def search():
    global ans

    if len(X) == N:
        ans = max(ans, calc())
        return

    for i in range(X[-1], M + 1):
        X.append(i)
        search()
        X.pop()

    return

for i in range(1, M + 1):
    X.append(i)
    search()
    X.pop()

print(ans)
