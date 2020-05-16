N, K = map(int, input().split())
D = set(map(str, range(10))) - set(list(input().split()))

for i in range(N, 100 * N):
    if set(list(str(i))) <= D:
        print(i)
        exit()

