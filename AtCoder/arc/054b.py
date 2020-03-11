P = float(input())
EPS = 1e-8

def f(x):
    return x + P * pow(2, -x / 1.5)

left = 0
right = P

while (right - left) > EPS:
    d = (right - left) / 3

    if f(left + d) < f(right - d):
        right -= d
    else:
        left += d

print('%.10f' % f(left))
