N = int(input())
M = 10**6 + 100

ims = [0] * (M)
for _ in range(N):
    l, r = map(int, input().split())
    ims[l] += 1
    ims[r + 1] -= 1

for i in range(1, M):
    ims[i] += ims[i - 1]

print(max(ims))
