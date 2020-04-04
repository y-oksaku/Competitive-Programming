from collections import Counter
S = Counter(input())

def isNotOk():
    WE = (S['W'] > 0) ^ (S['E'] > 0)
    NS = (S['N'] > 0) ^ (S['S'] > 0)
    return WE or NS

print('No' if isNotOk() else 'Yes')
