N = int(input())

C = [[]]
for _ in range(N):
    c = int(input())

    if len(C[-1]) > 0 and C[-1][0] != c:
        C.append([])
    C[-1].append(c)

if len(C) > 1 and C[0][0] == C[-1][0]:
    C[0].extend(C.pop())

if len(C) == 1:
    print(-1)
    exit()

ans = 0
for c in C:
    ans = max(ans, (len(c) - 1) // 2)
print(ans + 1)
