N, K = map(int, input().split())
A = list(map(int, input().split()))

def ceil(x, y) :
    return (x + y - 1) // y

ans = ceil(N - K, K - 1) + 1
print(ans)