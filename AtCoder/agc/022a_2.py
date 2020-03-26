import string
S = input()
alph = string.ascii_lowercase

if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

if set(S) == set(alph):
    L = []
    for i in range(len(S) - 1):
        T = S[:i]
        for a in alph:
            if not a in T and (T + a) > S[:i + 1]:
                L.append(T + a)
                break
    L.sort()
    print(L[0])
else:
    for a in alph:
        if not a in S:
            print(S + a)
            exit()
