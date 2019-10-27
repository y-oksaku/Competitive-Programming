L , R = map(int,input().split())

ans = float('inf')

for i in range(L, min(R+1,L+2020)) :
    for j in range(i+1,min(R+1,i+2020)) :
        ans = min(ans, (i*j) % 2019)

print(ans)