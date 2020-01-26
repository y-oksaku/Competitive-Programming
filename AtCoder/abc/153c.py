N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)

ans = sum(H) - sum(H[:K])
print(ans)