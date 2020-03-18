N = int(input())
P = list(map(lambda a: int(a) - 1, input().split()))

A = [i * (N + 1) for i in range(1, N + 1)]
B = [(N - i + 1) * (N + 1) for i in range(1, N + 1)]

for i, p in enumerate(P):
    A[p] += i

print(*A)
print(*B)
