from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

X = [tuple(p) for p in permutations(range(1, N + 1), r=N)]
X.sort()

print(abs(X.index(P) - X.index(Q)))
