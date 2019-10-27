N, K = map(int, input().split())
A = list(map(int, input().split()))

firstWin = [None] * (K + 1)

firstWin[0] = False

for k in range(K + 1):
    for a in A:
        if k - a >= 0:
            if firstWin[k - a] == False:
                firstWin[k] = True
                break
    else:
        firstWin[k] = False

if firstWin[K]:
    print('First')
else:
    print('Second')