N = int(input())
D = [int(input()) for _ in range(N)]

mx = sum(D)
mi = max(0, max(D) - (sum(D) - max(D)))
print(mx)
print(mi)
