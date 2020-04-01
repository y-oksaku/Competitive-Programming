N, K = map(int, input().split())
D = set(list(input()))

for k in range(N, 20 * N):
    if len(set(list(str(k))) & D) == 0:
        print(k)
        exit()
