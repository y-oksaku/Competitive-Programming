N = int(input())

def divisor(n):
    div = set()
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            div.add(i)
            div.add(n // i)
        i += 1
    return len(div)

ans = 0
for i in range(1, N + 1, 2):
    if divisor(i) == 8:
        ans += 1

print(ans)
