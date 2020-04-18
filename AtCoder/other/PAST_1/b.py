N = int(input())
A = [int(input()) for _ in range(N)]

ans = []
for a, b in zip(A[1:], A):
    if a == b:
        ans.append('stay')
        continue
    ans.append('{} {}'.format('up' if a > b else 'down', abs(a - b)))
print(*ans, sep='\n')
