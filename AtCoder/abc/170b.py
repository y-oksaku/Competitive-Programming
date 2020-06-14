X, Y = map(int, input().split())

for two in range(X + 1):
    four = X - two

    if two * 2 + four * 4 == Y:
        print('Yes')
        exit()

print('No')

