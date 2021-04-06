X, Y = map(int, input().split())
U, W = map(int, input().split())

dx, dy = abs(X - U), abs(Y - W)
ans = 2 if (X + Y) % 2 == (U + W) % 2 else 3

if dx + dy == 0:
    ans = min(ans, 0)

if dx + dy <= 3:
    ans = min(ans, 1)

if dx + dy <= 6:
    ans = min(ans, 2)

for a, b in ((U, Y + dx), (U, Y - dx), (X + dy, W), (X - dy, W)):
    da, db = abs(a - U), abs(b - W)

    if da + db == 0:
        ans = min(ans, 1)

    if da + db <= 3:
        ans = min(ans, 2)

print(ans)
