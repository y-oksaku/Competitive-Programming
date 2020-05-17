from math import pi as PI
from math import cos, sin

A, B, H, M = map(int, input().split())

thetaA = (H / 12) + (M / 60) * (1 / 12)
thetaB = (M / 60)

thetaA *= 2 * PI
thetaB *= 2 * PI

P = complex(A * cos(thetaA), A * sin(thetaA))
Q = complex(B * cos(thetaB), B * sin(thetaB))

print(abs(P - Q))
