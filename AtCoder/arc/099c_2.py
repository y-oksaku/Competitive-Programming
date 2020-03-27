N, K = map(int, input().split())
_ = input()

ans = 1
N -= K

if N > 0:
    ans += -(-N // (K - 1))

print(ans)
