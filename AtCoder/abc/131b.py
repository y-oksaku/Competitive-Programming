N , L = map(int,input().split())

taste = [0] * N

for i in range(1,N+1) :
    taste[i-1] = L + i - 1

taste.sort(key=lambda i : abs(i))

ans = sum(taste[1:N])

print(ans)