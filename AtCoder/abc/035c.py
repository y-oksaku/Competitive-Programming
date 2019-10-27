N, Q = map(int, input().split())

ism = [0 for _ in range(N + 2)]
for _ in range(Q):
    l, r = map(int, input().split())
    ism[l] += 1
    ism[r + 1] -= 1

count = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    count[i] = count[i - 1] + ism[i]

ans = []
for i in range(1, N + 1):
    if count[i] % 2 == 0:
        ans.append('0')
    else:
        ans.append('1')

print(''.join(ans))
