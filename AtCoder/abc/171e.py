N = int(input())
A = list(map(int, input().split()))

S = 0
for a in A:
    S ^= a

print(*[S ^ a for a in A])
