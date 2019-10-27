N = int(input())
bit = bin(N)[2:]
digit = len(bit)

if digit % 2 == 1:
    now = 1
    ans = True
    while now <= N:
        if ans:
            now = now * 2 + 1
        else:
            now = now * 2
        ans = not ans
else:
    now = 1
    ans = True
    while now <= N:
        if ans:
            now = now * 2
        else:
            now = now * 2 + 1
        ans = not ans

print('Takahashi' if ans else 'Aoki')
