from collections import Counter
N = int(input())
A = Counter([int(input()) for _ in range(N)])

x, y = -1, -1
for i in range(1, N + 1):
    if A[i] == 1:
        continue
    if A[i] == 0:
        x = i
    if A[i] == 2:
        y = i

if x == y == -1:
    print('Correct')
else:
    print(y, x)
