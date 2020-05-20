A, B = map(int, input().split())
S = input()
N = set(map(str, range(10)))

L = set(S[:A])
M = S[A]
R = set(S[-B:])

if (L | R) <= N and M == '-':
    print('Yes')
else:
    print('No')

