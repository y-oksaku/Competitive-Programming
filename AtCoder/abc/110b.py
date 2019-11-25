N, M, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if max(A + [X]) < min(B + [Y]):
    print('No War')
else:
    print('War')