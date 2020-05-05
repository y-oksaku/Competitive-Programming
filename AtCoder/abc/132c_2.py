N = int(input())
D = list(map(int, input().split()))
D.sort()

L, R = D[N // 2 - 1], D[N // 2]
print(R - L)
