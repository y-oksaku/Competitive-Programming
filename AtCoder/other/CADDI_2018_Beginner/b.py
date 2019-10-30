N, H, W = map(int, input().split())
AB = (tuple(map(int, input().split())) for _ in range(N))
print(sum((1 if a >= H and b >= W else 0 for a, b in AB)))