N = int(input())
A = [int(input()) for _ in range(N)]

isAllEven = True

for a in A:
    if a % 2 == 1:
        isAllEven = False
        break

if isAllEven:
    print('second')
else:
    print('first')