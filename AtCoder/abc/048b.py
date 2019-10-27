A, B, X = map(int, input().split())
if A % X != 0:
    A += X - A % X
B -= B % X

if A > B:
    print(0)
else:
    ans = (B - A) // X + 1
    print(ans)