N, X = map(int, input().split())
A = list(map(int, input().split()))

print(sum([a for i, a in enumerate(A) if (X & (1 << i)) != 0]))
