from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for _ in range(Q)]

A.reverse()

evenA = [0] * (N + 1)
accA = [0] * (N + 1)

for i in range(1, N + 1):
    evenA[i] = evenA[i - 1] + (A[i - 1] if i % 2 == 1 else 0)
    accA[i] = accA[i - 1] + A[i - 1]

borders = []
scores = []

for i in range(1, N // 2 + N % 2):
    border = (A[i] + A[i * 2]) // 2 + 1
    borders.append(border)

    score = accA[i] + (evenA[N] - evenA[i * 2])
    scores.append(score)

scores.append(accA[N // 2 + N % 2])

borders.reverse()
scores.reverse()

for x in X:
    i = bisect_right(borders, x)
    print(scores[i])
