from math import sin, pi
print(pi)
A, B, C = map(int, input().split())

def f(t):
    return A * t + B * sin(C * t * pi)

less = 0
overEq = 10**18
for _ in range(1000):
    mid = (less + overEq) / 2
    if f(mid) >= 100:
        overEq = mid
    else:
        less = mid

print(overEq)