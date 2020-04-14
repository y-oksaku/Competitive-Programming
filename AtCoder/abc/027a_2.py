L = list(map(int, input().split()))

for l in L:
    if L.count(l) % 2 == 1:
        print(l)
        exit()
