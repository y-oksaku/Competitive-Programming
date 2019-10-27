N, A, B = map(int, input().split())
items = list(map(int, input().split()))

items.sort(reverse=True)

maxAvg = sum(items[:A]) / A

print(maxAvg)

fact = [1 for _ in range(N + 10)]

for i in range(1, N + 10):
    fact[i] = (fact[i - 1] * i)

def comb(n, r):
    if 0 < r < n:
        return fact[n] // fact[r] // fact[n - r]
    if r == 0 or r == n:
        return 1
    return 0


if items[0] == items[A - 1]:
    right = A - 1
    while right < N and items[right] == items[0]:
        right += 1
    ans = 0
    for take in range(A, B + 1):
        ans += comb(right, take)
    print(ans)
else:
    left = A - 1
    while left >= 0 and items[left] == items[A - 1]:
        left -= 1
    right = A - 1
    while right < N and items[right] == items[A - 1]:
        right += 1
    ans = comb(right - left - 1, A - left - 1)
    print(ans)