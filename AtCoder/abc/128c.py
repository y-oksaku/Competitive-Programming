N , M = map(int,input().split())

# 電球
k = []
s = []


for i in range(M):
    I = input().split()

    k.append(I.pop(0))
    s.append(list(map(int,I)))


P = list(map(int , input().split()))
status = [0]*N

count = 0

for i in range(2**N):
    flag = True

    binary = i
    for j in range(N):
        status[j] = 1 if (binary % 2 == 1) else 0
        binary = int(binary / 2)

    for j in range(M):
        sum = 0
        for index in s[j]:
            sum = sum + status[index-1]

        if sum % 2 != P[j]:
            flag = False
            break

    if flag:
        count = count + 1


print(count)