A = [tuple(map(int, input().split())) for _ in range(3)]
N = int(input())
B = set()
for _ in range(N):
    B.add(int(input()))

X = [
    set(A[0]),
    set(A[1]),
    set(A[2]),
    set([A[0][0], A[1][0], A[2][0]]),
    set([A[0][1], A[1][1], A[2][1]]),
    set([A[0][2], A[1][2], A[2][2]]),
    set([A[0][0], A[1][1], A[2][2]]),
    set([A[0][2], A[1][1], A[2][0]]),
]

for x in X:
    if x <= B:
        print('Yes')
        exit()

print('No')