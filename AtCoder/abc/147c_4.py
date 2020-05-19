N = int(input())
A = []
for _ in range(N):
    S = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        S.append((x - 1, y))
    A.append(S)

def calc(state):
    ret = 0
    for i, S in enumerate(A):
        if (state & (1 << i)) == 0:
            continue
        ret += 1
        for x, y in S:
            if (state & (1 << x)) != (y << x):
                return 0
    return ret

ans = 0
for state in range(1 << N):
    ans = max(ans, calc(state))
print(ans)
