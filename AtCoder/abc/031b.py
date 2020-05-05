L, H = map(int, input().split())
N = int(input())

for _ in range(N):
    a = int(input())
    if a > H:
        print(-1)
    elif a < L:
        print(L - a)
    else:
        print(0)

