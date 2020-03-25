N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
N -= K

if N > 0:
    ans += -(-N // (K - 1))

print(ans)