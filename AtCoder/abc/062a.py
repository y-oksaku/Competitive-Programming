x, y = map(int, input().split())
A = set([1, 3, 5, 7, 8, 10, 12])
B = set([4, 6, 9, 11])
C = set([2])

for S in [A, B, C]:
    if x in S and y in S:
        print('Yes')
        break
else:
    print('No')
