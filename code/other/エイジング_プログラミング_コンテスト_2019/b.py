N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

one = 0
two = 0
for p in P:
    if p <= A:
        one += 1
    elif A < p <= B:
        two += 1

print(min(one, two, N - (one + two)))