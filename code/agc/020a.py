N, A, B = map(int, input().split())

if abs(A - B - 1) % 2 == 0:
    print('Borys')
else:
    print('Alice')