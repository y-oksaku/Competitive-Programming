N , A , B = map(int,input().split())

ans = 0

for i in range(1,N+1) :
    value = i
    sp = []
    while value != 0 :
        sp.append(value % 10)
        value = int(value / 10)

    sumValue = sum(sp)

    if(sumValue >= A and sumValue <= B) :
        ans += i

print(ans)