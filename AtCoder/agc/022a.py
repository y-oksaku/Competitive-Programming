import string

S = input()
V = set(S)

for s in string.ascii_lowercase:
    if not s in V:
        print(S + s)
        exit()

for s, t in zip(S[:: -1], string.ascii_lowercase):
    if s != t:
        break
else:
    print(-1)
    exit()

for i in range(len(S))[:: -1]:
    A = []
    for j in range(i + 1, len(S)):
        if S[i] < S[j]:
            A.append(S[j])
    if A:
        A.sort()
        print(S[: i] + A[0])
        break