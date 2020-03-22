S = input()
N = len(S)

def isOk(s):
    for s, t in zip(s, s[:: -1]):
        if s != t:
            return False
    return True

for s in [S, S[:(N - 1) // 2], S[(N + 3) // 2 - 1:]]:
    if not isOk(s):
        print('No')
        exit()

print('Yes')