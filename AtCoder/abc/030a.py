A, B, C, D = map(int, input().split())

if B * C < D * A:
    print('AOKI')
elif B * C > D * A:
    print('TAKAHASHI')
else:
    print('DRAW')
