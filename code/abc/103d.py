N, M = map(int, input().split())

war = []

for _ in range(M) :
    A, B = map(int, input().split())
    war.append((A,B))

war.sort(key=lambda A : A[0])

ans = 1
left, right = war[0]

for i in range(1, M) :
    A, B = war[i]
    if right <= A :
        ans += 1
        left = A
        right = B
        continue
    left = A
    right = min(right, B)

print(ans)
