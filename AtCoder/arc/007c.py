S = input()
N = len(S)

A = 0
for s in S:
    A *= 2
    A |= (s == 'o')
mask = (1 << N) - 1

ans = 10
for I in range(1 << N):
    state = A
    cnt = 1
    for i in range(1, N):
        if (I & (1 << i)) == 0:
            continue
        cnt += 1
        state |= (A << (N - i)) & mask
        state |= (A >> i) & mask
    if state == mask:
        ans = min(ans, cnt)

print(ans)
