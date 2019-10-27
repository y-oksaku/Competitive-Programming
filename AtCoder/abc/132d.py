N , K = map(int,input().split())

M = N - K

fact = [1] * (N+1)

for i in range(1,N+1) :
    fact[i] = fact[i-1] * i

def p(n,r) :
    return fact[n] // fact[n-r]

def combi(n,r) :
    return p(n,r) // fact[r]

for i in range(1,K+1) :
    if i-1 > N-K :
        print(0)
        continue

    blue = max(combi(K-1,i-1),1)
    red = max(combi(M+1,i),1)

    print(red * blue % (10**9 + 7))

