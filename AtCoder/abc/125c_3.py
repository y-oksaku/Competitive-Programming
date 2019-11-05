N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

leftGcd = [-1] * (N + 1)
leftGcd[0] = A[0]
for i, a in enumerate(A, start=1):
    leftGcd[i] = gcd(leftGcd[i - 1], a)

rightGcd = [-1] * (N + 1)
rightGcd[-1] = A[-1]
for i, a in enumerate(A[:: -1], start=2):
    rightGcd[-i] = gcd(rightGcd[-i + 1], a)

ans = max(leftGcd[-2], rightGcd[1])
for mid in range(N):
    ans = max(ans, gcd(leftGcd[mid], rightGcd[mid + 1]))

print(ans)