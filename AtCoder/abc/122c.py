N , Q = map(int,input().split())
S = input()

count = [0] * (N + 1)

for i in range(N) :
    count[i+1] = count[i] + (1 if S[i:i+2] == 'AC' else 0)

ans = [0] * Q

for i in range(Q) :
    l , r = map(int,input().split())
    ans[i] = count[r-1] - count[l-1]

for a in ans :
    print(a)



