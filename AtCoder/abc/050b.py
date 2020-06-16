N = int(input())
T = list(map(int, input().split()))
M = int(input())

S = sum(T)
for _ in range(M):
    p, x = map(int, input().split())
    p -= 1
    print(S - T[p] + x)
