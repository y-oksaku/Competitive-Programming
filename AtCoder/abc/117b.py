N = int(input())
L = list(map(int, input().split()))
mx = max(L)

if sum(L) - mx > mx:
    print('Yes')
else:
    print('No')