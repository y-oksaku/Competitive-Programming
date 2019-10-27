K = int(input())
N = 50

q, r = divmod(K, N)

ans = [q + (N - 1) - r] * (50 - r) + [q + (N - 1) + N - (r - 1)] * r

print(50)
print(*ans)