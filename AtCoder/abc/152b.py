a, b = map(int, input().split())

A = ''.join([str(a)] * b)
B = ''.join([str(b)] * a)

if A <= B:
    print(A)
else:
    print(B)