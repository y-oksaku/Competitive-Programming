H, W, A, B = map(int ,input().split())

ans = []
b = 0

for _ in range(H):
    if b < B:
        ans.append(''.join(map(str, [1] * A + [0] * (W - A))))
        b += 1
    else:
        ans.append(''.join(map(str, [0] * A + [1] * (W - A))))

print(*ans, sep='\n')