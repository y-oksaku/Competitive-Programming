N = int(input())
A = list(map(int, input().split()))

last = 0

for i in range(N-1) :
    last = last ^ A[i]

if last == A[-1] :
    print('Yes')
else :
    print('No')