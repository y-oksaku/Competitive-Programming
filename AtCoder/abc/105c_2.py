N = int(input())

if N == 0:
    print(0)
    exit()

ans = []
while N != 0:
    d = len(ans)
    if N % 2 == 1:
        ans.append('1')
        N -= pow(-1, d)
        N //= 2
    else:
        ans.append('0')
        N //= 2

print(''.join(ans[::-1]))
