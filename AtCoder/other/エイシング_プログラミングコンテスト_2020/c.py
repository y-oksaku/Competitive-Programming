from itertools import product

N = int(input())

ans = [0] * (N + 1)
for x, y, z in product(range(1, 101), repeat=3):
    f = x**2 + y**2 + z**2 + x * y + y * z + z * x
    if f <= N:
        ans[f] += 1

print(*ans[1:], sep='\n')
