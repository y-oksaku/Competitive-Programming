m, n, N = map(int, input().split())

ans = N
stock = N

while stock >= m:
    pair, stock = divmod(stock, m)
    ans += pair * n
    stock += pair * n

print(ans)