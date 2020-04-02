N = int(input())

ans = N - 1
for i in range(1, int(N**0.5) + 100):
    if N % i != 0:
        continue
    j = N // i
    ans = min(ans, i + j - 2)
print(ans)
