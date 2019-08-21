A , B = map(int,input().split())

ans = 0

if A == B :
    ans = A + A
else :
    ans = 2 * max(A,B) - 1

print(ans)