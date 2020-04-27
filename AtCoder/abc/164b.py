A, B, C, D = map(int, input().split())

for i in range(1000):
    if i % 2 == 0:
        C -= B
    else:
        A -= D

    if min(A, C) <= 0:
        print('Yes' if i % 2 == 0 else 'No')
        break
