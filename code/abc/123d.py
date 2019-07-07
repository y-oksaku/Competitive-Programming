from heapq import heappop , heappush

X , Y , Z , K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# それぞれソート
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

# 処理済みフラグ
confilm = []

q = [(-(A[0] + B[0] + C[0]) , 0,0,0)]

for _ in range(K) :
    val , i , j , k = heappop(q)

    print(-val)

    t = (i+1,j,k)
    if i + 1 < X and not t in confilm :
        heappush(q,(-(A[i+1] + B[j] + C[k]),) + t)
        confilm.append(t)

    t = (i,j+1,k)
    if j + 1 < Y and not t in confilm :
        heappush(q,(-(A[i] + B[j+1] + C[k]),) + t)
        confilm.append(t)

    t = (i,j,k+1)
    if k + 1 < Z and not t in confilm :
        heappush(q,(-(A[i] + B[j] + C[k+1]),) + t)
        confilm.append(t)


