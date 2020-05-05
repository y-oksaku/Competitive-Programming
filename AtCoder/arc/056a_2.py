A, B, K, L = map(int, input().split())

l = K // L

ans = min(
    l * B + (K - l * L) * A,
    (l + 1) * B,
    A * K
)

print(ans)
