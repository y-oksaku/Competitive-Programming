N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans = 0

for i, h in enumerate(H):
    if abs((T - 0.006 * H[ans]) - A) > abs((T - 0.006 * h) - A):
        ans = i

print(ans + 1)