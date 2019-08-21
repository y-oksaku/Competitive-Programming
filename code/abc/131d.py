N = int(input())

time = [0] * N

for i in range(N) :
    time[i] = list(map(int,input().split()))


# 締め切り順
time.sort(key=lambda A : A[1])

now = 0
for i in range(N) :
    now += time[i][0]
    if now > time[i][1] :
        print('No')
        break
else :
    print('Yes')