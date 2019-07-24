N = int(input())
A = list(map(int, input().split()))

ball = [0] * N
ans = []

for i in range(1, N+1) :
    ballCount = sum(ball[N-i::N-i+1])
    if ballCount % 2 == A[N-i] :
        pass
    else :
        ball[N - i] = 1
        ans.append(N - i + 1)
print(len(ans))
print(*ans)
