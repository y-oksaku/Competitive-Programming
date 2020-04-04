N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

cnt = 0
for a in A:
    if S <= a * 4 * M:
        cnt += 1

print('Yes' if cnt >= M else 'No')
