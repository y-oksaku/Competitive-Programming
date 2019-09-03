A = input()
N = len(A)

if N == 1:
    print(0)
    exit()

sameIndexPair = set()
diffIndexPair = set()

for i, (s, t) in enumerate(zip(A, A[:: -1])):
    if s == t:
        sameIndexPair.add((min(i, N - 1 - i), max(i, N - 1 - i)))
    else:
        diffIndexPair.add((min(i, N - 1 - i), max(i, N - 1 - i)))

ans = 0
for i, j in sameIndexPair:
    if i == j:
        if len(diffIndexPair) > 0:
            ans += 25
    else:
        ans += 50

if len(diffIndexPair) == 1:
    ans += 24 * 2
elif len(diffIndexPair) > 1:
    ans += 25 * len(diffIndexPair) * 2

print(ans)