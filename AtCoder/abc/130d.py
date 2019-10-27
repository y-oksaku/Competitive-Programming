N , K = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
right = 0
now = 0

while right < N :
    if now >= K :
        break
    now += a[right]
    right += 1

if now < K :
    print(0)
else :
    ans += N - right + 1

    for i in range(N) : # 左端(含めない)
        now -= a[i]
        if now >= K :
            ans += N - right + 1
        else :
            while right < N :
                now += a[right]
                right += 1
                if now >= K :
                    break
            else :
                break
            ans += N - right + 1

    print(ans)