N = int(input())
A = list(map(int, input().split()))
A = [a for a in A if a % 2 == 0]

if all(a % 3 == 0 or a % 5 == 0 for a in A):
    print('APPROVED')
else:
    print('DENIED')
