N = int(input())

sList = {}

for i in range(N) :
    s = list(input())
    s.sort()
    s = ''.join(s)

    if s in sList :
        sList[s] += 1
    else :
        sList[s] = 1

ans = 0
for _, num in sList.items() :
    ans += num * (num - 1) // 2

print(ans)
