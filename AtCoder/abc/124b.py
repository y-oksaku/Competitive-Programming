N = int(input())
H = list(map(int,input().split()))

maxHeight = 0
ans = 0

for height in H :
    if height >= maxHeight :
        ans += 1
    maxHeight = max(maxHeight,height)

print(ans)