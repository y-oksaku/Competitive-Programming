N = int(input())

def digit(x, base):
    if x == 0:
        return 0
    return digit(x // base, base) + x % base

def calc(six, nine):
    return digit(six, 6) + digit(nine, 9)

ans = 10**18
for six in range(N + 1):
    ans = min(ans, calc(six, N - six))
print(ans)