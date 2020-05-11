from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

if len(A.keys()) >= 3:
    print('No')
    exit()

if len(A.keys()) == 1:
    p = list(A.keys())[0]
    print('Yes' if 2 * p <= N or p == N - 1 else 'No')
    exit()

p1, p2 = sorted(A.keys())
print('Yes' if p2 - p1 == 1 and (A[p1] + 1) <= p2 <= (A[p1] + A[p2] // 2) else 'No')
