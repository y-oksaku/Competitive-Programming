N = int(input())
W = [input() for _ in range(N)]
V = set()
prev = -1
for S in W:
    if S in V:
        print('No')
        exit()
    V.add(S)
    if prev == -1 or S[0] == prev:
        prev = S[-1]
    else:
        print('No')
        exit()
print('Yes')