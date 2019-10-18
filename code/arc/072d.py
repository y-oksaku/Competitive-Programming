X, Y = map(int, input().split())

if max(X, Y) <= 1:
    print('Brown')
    exit()

if abs(X - Y) <= 1:
    print('Brown')
else:
    print('Alice')