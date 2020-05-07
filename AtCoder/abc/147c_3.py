N = int(input())
A = []

for _ in range(N):
    A.append([tuple(map(int, input().split())) for _ in range(int(input()))])

def exists(state):
    ret = 0
    for i in range(N):
        if ((1 << i) & state) == 0:
            continue
        ret += 1
        for x, y in A[i]:
            if ((state & (1 << (x - 1))) > 0) != (y > 0):
                return 0
    return ret

ans = 0
for state in range(1 << N):
    ans = max(ans, exists(state))
print(ans)
