from functools import lru_cache
N = int(input())

A = []
B = []
food = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    food.append((a + b, i))

food.sort(reverse=True)
X = 0
Y = 0
cnt = 0

for _, i in food:
    if cnt % 2 == 0:
        X += A[i]
    else:
        Y += B[i]
    cnt += 1

print(X - Y)