N, Y = map(int, input().split())

for man in range(Y // 10000 + 1):
    for go in range(Y // 5000 + 1):
        X = Y - man * 10000 - go * 5000
        if X < 0:
            continue
        sen = X // 1000
        if man + go + sen == N:
            print(man, go, sen)
            exit()

print('-1 -1 -1')