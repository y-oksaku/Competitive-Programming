N = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)

Alice = 0
Bob = 0

for i in range(int(N/2)) :
    Alice += a.pop(0)
    Bob += a.pop(0)

if len(a) > 0 :
    Alice += a.pop()

print(Alice - Bob)