import math
import copy

N = int(input())

if N == 1 :
    print(1)
else :
    ball = [0] * N

    for i in range(N) :
        ball[i] = list(map(int,input().split()))

    ans = N - 1
    pq = []

    # p,q の組
    for i in range(N) :
        for j in range(N) :
            p = ball[j][0] - ball[i][0]
            q = ball[j][1] - ball[i][1]

            if p == 0 and q == 0 :
                continue
            pq.append((p,q))

    ans = N - 1

    for p , q in pq :
        check = [0] * N
        count = 0

        for i in range(N) :
            if check[i] == 0 :
                check[i] = 1
                count += 1
                for j in range(1,N) : # 上
                    if [ball[i][0] - j * p , ball[i][1] - j * q] in ball :
                        index = ball.index([ball[i][0] - j * p , ball[i][1] - j * q])
                        check[index] = 1
                    else :
                        break
                for j in range(1,N) : # 下
                    if [ball[i][0] + j * p , ball[i][1] + j * q] in ball :
                        index = ball.index([ball[i][0] + j * p , ball[i][1] + j * q])
                        check[index] = 1
                    else :
                        break
        ans = min(ans,count)
    print(ans)