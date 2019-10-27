from collections import defaultdict

N = int(input())
M = int(input())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

G = gcd(N, M)
N //= G
M //= G

if M == 1:
    for s in str(N)[:: -1]:
        if s != '0':
            print(s)
            exit()

# 10の約数(2, 5)以外を持つと無限小数
primeCnt = {2 : 0, 5 : 0}
while M % 5 == 0:
    primeCnt[5] += 1
    M //= 5
while M % 2 == 0:
    primeCnt[2] += 1
    M //= 2

if M > 1:
    print(-1)
else:
    if primeCnt[2] == primeCnt[5]:
        print(str(N)[-1])
    elif primeCnt[2] > primeCnt[5]:
        primeCnt[2] -= primeCnt[5]
        while primeCnt[2] > 0 and N % 2 == 0:
            N //= 2
            primeCnt[2] -= 1
        if primeCnt[2] == 0:
            print(str(N)[-1])
        else:
            print(5)
    else:
        primeCnt[5] -= primeCnt[2]
        while primeCnt[5] > 0 and N % 5 == 0:
            N //= 5
            primeCnt[5] -= 1
        if primeCnt[5] == 0:
            print(str(N)[-1])
        else:
            ans = (N % 5) * 2
            primeCnt[5] -= 1
            ans *= pow(2, primeCnt[5], 10)
            print(str(ans)[-1])

