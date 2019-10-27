A, B = map(int, input().split())

strA = str(A)
strB = str(B)

ans = max(
    A - B,
    A - B + (9 - int(strA[0])) * 10**(len(strA) - 1),
)

if 100 <= B <= 199:
    if 100 <= B <= 109:
        C = 100
    else:
        C = B - (int(strB[1])) * 10
else:
    C = B - (int(strB[0]) - 1) * 100

if 900 <= A <= 999:
    if 990 <= A <= 999:
        D = 999
    else:
        D = A + (9 - int(strA[1])) * 10
else:
    D = A + (9 - int(strA[0])) * 100

ans = max(ans, A - C)
ans = max(ans, D - B)

print(ans)