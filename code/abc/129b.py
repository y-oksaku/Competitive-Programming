N = int(input())
W = list(map(int,input().split()))

S = [1000000000] * (N+1)

for i in range(1,N) :
    S1 = W[:i]
    S2 = W[i:]

    S[i] = abs(sum(S1) - sum(S2))

S.sort()

print(S[0])