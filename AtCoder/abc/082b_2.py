S = list(input())
T = list(input())

S.sort()
T.sort(reverse=True)

print('Yes' if S < T else 'No')
