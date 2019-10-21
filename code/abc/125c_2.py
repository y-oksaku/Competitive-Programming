N = int(input())
A = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

leftGcd = [-1] * (N + 1)
leftGcd[0] = A[0]

for i, a in enumerate(A, start=1):
    leftGcd[i] = gcd(leftGcd[i - 1], a)

rightGcd = [-1] * (N + 1)
rightGcd[-1] = A[-1]

for i, a in enumerate(reversed(A), start=1):
    rightGcd[-(i + 1)] = gcd(rightGcd[-i], a)

ans = max(rightGcd[1], leftGcd[-2])
for mid in range(1, N):
    ans = max(ans, gcd(leftGcd[mid], rightGcd[mid + 1]))

print(ans)