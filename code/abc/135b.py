N = int(input())
P = list(map(int, input().split()))

count = 0
for i in range(N) :
    if P[i] != (i + 1) :
        count += 1

if count >= 3 :
    print('NO')
else :
    print('YES')