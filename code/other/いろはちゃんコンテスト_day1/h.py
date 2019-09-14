N = int(input())

if N < 10:
    ans = 10 + (N - 1)
    print(ans)
    exit()

def f(n):
    ret = 0
    for i in str(n):
        ret += int(i)
    return ret

fN = f(N)

ans = 0
digit = 1
while f(ans) + 9 < fN:
    ans += 9 * digit
    digit *= 10

if ans + (fN - f(ans)) * digit != N:
    ans += (fN - f(ans)) * digit
elif fN - f(ans) == 9:
    ans += 18 * digit
else:
    ans -= (digit // 10)
    ans += digit * (fN - f(ans))

print(ans)