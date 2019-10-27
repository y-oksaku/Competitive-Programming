N = input()
numberList = list(map(int,input().split()))

ans = numberList[0]

for number in numberList:
    binary = bin(number)
    for k in range(1,len(binary)+1):
        if binary[-k] == '1':
            ans = min(ans,k-1)
            break

print(ans)