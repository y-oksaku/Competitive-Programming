from fractions import Fraction

n , a , b , c = map(int,input().split())

A = 0
kA = 0
B = 0
kB = 0

for k in range(1,n) :
    A += a**k
    kA += k * a**k
    B += b**k
    kB += k * b**k

e = A * ( (1/c) * kB + (c/(1-c)**2) * B ) + B * ( (1/c) * kA + (c/(1-c)**2) * A )

print(e)

frac = Fraction(e)

print(frac)