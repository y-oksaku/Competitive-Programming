N = int(input())
C = [[]]

for _ in range(N):
    c = int(input())
    if len(C[-1]) > 0 and C[-1][-1] != c:
        C.append([])
    C[-1].append(c)

if len(C) == 1:
    print(-1)
else:
    if C[0][0] == C[-1][-1]:
        C[0].extend(C.pop())
    print(max(-(-len(c) // 2) for c in C))
