A, B = map(int, input().split())

A = (A - 2) % 13
B = (B - 2) % 13

if A == B:
    print('Draw')
elif A < B:
    print('Bob')
else:
    print('Alice')