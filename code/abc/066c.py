N = int(input())
A = list(map(int, input().split()))

oddA = A[::2]
evenA = A[1::2]

if N % 2 == 1:
    ans = list(reversed(oddA)) + evenA
else:
    ans = list(reversed(evenA)) + oddA

print(*ans)