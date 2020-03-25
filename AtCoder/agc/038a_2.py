H, W, A, B = map(int, input().split())

L = ''.join(['1'] * A + ['0'] * (W - A))
R = ''.join(['0'] * A + ['1'] * (W - A))

ans = []
for h in range(H):
    if h < B:
        ans.append(L)
    else:
        ans.append(R)

print(*ans, sep='\n')