N, M = map(int,input().split())

# S:N, c:M
# c+c = S

if M < 2*N :
    print(M // 2)
else :
    ans = N
    r = M - 2 * N  # 残り個数

    ans += r // 4  # (c + c)cc で一つ

    print(ans)