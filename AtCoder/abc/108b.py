x1, y1, x2, y2 = map(int, input().split())
v = (x2 - x1, y2 - y1)

x3, y3 = x2 - v[1], y2 + v[0]
x4, y4 = x3 - v[0], y3 - v[1]
print(x3, y3, x4, y4)
