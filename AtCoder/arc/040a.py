N = int(input())
blue = 0
red = 0
for _ in range(N):
    S = input()
    for s in S:
        if s == 'R':
            red += 1
        elif s == 'B':
            blue += 1

if blue < red:
    print('TAKAHASHI')
elif red < blue:
    print('AOKI')
else:
    print('DRAW')
