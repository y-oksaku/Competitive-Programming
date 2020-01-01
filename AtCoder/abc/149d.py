N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

points = {
    'r' : P,
    's' : R,
    'p' : S
}

ans = 0
for t in T:
    ans += points[t]

for k in range(K):
    left = k
    while left < N:
        right = left
        while right < N and T[right] == T[left]:
            right += K
        cnt = (right - left) // K
        ans -= points[T[left]] * (cnt // 2)
        left = right
print(ans)
