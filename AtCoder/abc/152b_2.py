a, b = map(int, input().split())

S = [str(a) * b, str(b) * a]
S.sort()
print(S[0])
