K, N = map(int, input().split())
A = list(map(int, input().split()))
B = [abs(x - y) for x, y in zip(A[1:], A)]
B += [K - A[-1] + A[0]]

print(sum(B) - max(B))
