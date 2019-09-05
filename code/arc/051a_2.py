Cx, Cy, r = map(int, input().split())
L, D, R, T = map(int, input().split())

if Cx - r >= L and Cx + r <= R and Cy - r >= D and Cy + r <= T:
    print('NO')
else:
    print('YES')

if (L - Cx)**2 + (T - Cy)**2 <= r**2 and (L - Cx)**2 + (D - Cy)**2 <= r**2 and (R - Cx)**2 + (T - Cy)**2 <= r**2 and (R - Cx)**2 + (D - Cy)**2 <= r**2:
    print('NO')
else:
    print('YES')