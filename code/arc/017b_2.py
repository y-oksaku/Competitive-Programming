N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

leng = 0
prev = -float('inf')
ans = 0

for a in A:
    if a > prev:
        leng += 1
    else:
        leng = 1
    if leng >= K:
        ans += 1
    prev = a

print(ans)
