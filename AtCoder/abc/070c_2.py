from itertools import product

A, B, C, D = map(int, input())

for p in product((1, -1), repeat=3):
    cnt = A
    for s, i in zip(p, (B, C, D)):
        cnt += s * i
    if cnt == 7:
        ans = str(A)
        for s, i in zip(p, (B, C, D)):
            ans += ('+' if s > 0 else '-') + str(i)
        ans += '=7'
        print(ans)
        exit()

print('-1')
