Q, H, S, D = map(int, input().split())
N = int(input())

# Q : 1
# H : 2
# S : 4
# D : 8
N *= 4
ans = 0

price = [(Q / 1, 1, Q), (H / 2, 2, H), (S / 4, 4, S), (D / 8, 8, D)]
price.sort()

for _, n, p in price:
    cnt = N // n
    ans += cnt * p
    N -= cnt * n

print(ans)
