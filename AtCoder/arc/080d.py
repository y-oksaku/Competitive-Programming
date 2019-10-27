H , W = map(int,input().split())
N = int(input())

A = list(map(int,input().split()))

ans = [0] * (H * W)

index = 0

for color , a in enumerate(A) :
    for _ in range(a) :
        ans[index] = color + 1
        index += 1

for i in range(H) :
    sub = ans[i * W : (i + 1) * W]
    if i % 2 == 0 :
        for j in range(W) :
            print('{} '.format(sub[j]), end='')
    else :
        sub.reverse()
        for j in range(W) :
            print('{} '.format(sub[j]), end='')
    print('')
