N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for left in range(K + 1):
    for right in range(K + 1):
        if left + right > K or left + right > N:
            break

        diff = K - left - right
        takes = V[:left] + V[N - right:]
        takes.sort(reverse=True)

        while diff > 0 and takes and takes[-1] < 0:
            takes.pop()
            diff -= 1

        ans = max(ans, sum(takes))

print(ans)