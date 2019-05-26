N , Q = map(int,input().split())

S = [0]*N
T = [0]*N
X = [0]*N
D = [0]*Q

for i in range(N):
    Input = list(map(int,input().split()))
    S[i] = Input[0]
    T[i] = Input[1]
    X[i] = Input[2]

for i in range(Q):
    D[i] = int(input())