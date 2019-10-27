A, B = map(int, input().split())

if A == B:
    print(A)
    exit()

ans = 0
if A % 2 == 1:
    ans ^= A
    A += 1

if (B - A + 1) % 2 == 1:
    ans ^= B
    B -= 1

if ((B - A + 1) // 2) % 2 == 1 and A <= B:
    ans ^= 1

print(ans)