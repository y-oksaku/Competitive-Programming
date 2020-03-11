import sys
input = sys.stdin.buffer.readline

A, B, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

XYC = [tuple(map(int, input().split())) for _ in range(M)]

ans = min(A) + min(B)
for x, y, c in XYC:
    cost = A[x - 1] + B[y - 1] - c
    ans = min(ans, cost)

print(ans)
