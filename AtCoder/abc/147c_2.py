N = int(input())

S = []
for _ in range(N):
    A = int(input())
    S.append([tuple(map(int, input().split())) for _ in range(A)])

def sol(state):
    for i, A in enumerate(S):
        if (state & (1 << i)) == 0:
            continue
        for j, s in A:
            if ((state & (1 << (j - 1))) != 0) != (s != 0):
                return 0
    return sum(map(int, bin(state)[2:]))

ans = 0
for state in range(1 << N):
    ans = max(ans, sol(state))
print(ans)
