from itertools import permutations

N = int(input())

R = set()
G = set()
B = set()
for i, s in enumerate(input(), start=1):
    if s == 'R':
        R.add(i)
    if s == 'G':
        G.add(i)
    if s == 'B':
        B.add(i)

ans = len(R) * len(G) * len(B)

def calc(A, B, C):
    ret = 0
    for a in A:
        for b in B:
            c = 2 * a - b
            if c in C:
                ret += 1
    return ret

ans -= calc(R, G, B)
ans -= calc(G, B, R)
ans -= calc(B, R, G)

print(ans)
