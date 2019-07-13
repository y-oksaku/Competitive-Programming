# MODにおける逆元
def modInv(a, MOD=1000000007) :
    b = MOD
    u = 1
    v = 0
    while b :
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u
    u = u % MOD
    return u
