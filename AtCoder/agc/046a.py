from math import gcd
X = int(input())

def lcm(n, m):
    return n * m // gcd(n, m)

print(lcm(X, 360) // X)
