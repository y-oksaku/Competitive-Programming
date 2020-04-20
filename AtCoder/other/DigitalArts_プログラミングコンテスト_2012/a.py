S = list(input().split())
N = int(input())

def isSame(S, T):
    if len(S) != len(T):
        return False

    for s, t in zip(S, T):
        if s != t and t != '*':
            return False

    return True

for _ in range(N):
    c = input()
    for i, s in enumerate(S):
        if isSame(s, c):
            S[i] = '*' * len(s)

print(*S)
