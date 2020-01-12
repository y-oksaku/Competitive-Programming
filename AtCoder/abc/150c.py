from itertools import permutations

N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

P = []
for perm in permutations(range(1, N + 1), r=N):
    P.append(tuple(perm))

P.sort()
print(abs(P.index(A) - P.index(B)))