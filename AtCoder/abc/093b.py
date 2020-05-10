A, B, K = map(int, input().split())
ans = set()

for i in range(K):
    ans.add(A + i)
    ans.add(B - i)
ans = [a for a in ans if A <= a <= B]
print(*sorted(ans), sep='\n')

