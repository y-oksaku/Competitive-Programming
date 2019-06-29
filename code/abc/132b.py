n = int(input())
p = list(map(int,input().split()))

ans = 0

for i in range(1,n-1) :
    s = p[i-1:i+2]

    s.sort()

    if s[1] == p[i] :
        ans += 1

print(ans)