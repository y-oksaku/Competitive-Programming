N, A, B, C, D = map(int, input().split())
S = '$' + input() + '$'

def isOk(fr, to):
    if S[fr: to + 1].count('##') > 0:
        return False
    return True

if not (isOk(A, C) and isOk(C, D)):
    print('No')
    exit()

def canSwitch():
    if S[max(A, B) - 1: min(C, D) + 2].count('...'):
        return True
    return False

if A < B and D < C or B < A and C < D:
    if not canSwitch():
        print('No')
        exit()

print('Yes')
