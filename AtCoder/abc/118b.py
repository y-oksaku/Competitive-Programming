N , M = map(int,input().split())

food = [0] * M

for i in range(N) :
    A = list(map(int,input().split()))
    for index in A[1:] :
        food[index-1] += 1

ans = 0
for count in food :
    if count >= N :
        ans += 1

print(ans)