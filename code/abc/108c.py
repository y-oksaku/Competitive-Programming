N, K = map(int, input().split())

ans = 0

ans += (N // K)**3

if K % 2 == 0 :
    ans += ((N - K // 2) // K + 1)**3

print(ans)