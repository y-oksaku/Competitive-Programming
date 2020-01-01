A, B, K = map(int, input().split())

C = max(0, A - K)
K -= A - C
print(C, max(0, B - K))