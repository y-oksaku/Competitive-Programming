x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def dist(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

a = dist(x1, y1, x2, y2)
b = dist(x2, y2, x3, y3)
c = dist(x3, y3, x1, y1)
s = (a + b + c) / 2

S = (s * (s - a) * (s - b) * (s - c))**0.5
leng = a + b + c
L = max(a, b, c)

r = S * 2 / leng
ans = r * L / (r + r + L)
print(ans)