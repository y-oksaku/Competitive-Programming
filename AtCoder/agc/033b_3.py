H, W, N = map(int, input().split())
sh, sw = map(int, input().split())
S = input()
T = input()

left = 0
right = W + 1
up = 0
down = H + 1

for s, t in zip(S[::-1], T[::-1]):
    if left + 1 >= right or up + 1 >= down:
        break

    if t == 'L':
        right = min(W + 1, right + 1)
    if t == 'R':
        left = max(0, left - 1)
    if t == 'U':
        down = min(H + 1, down + 1)
    if t == 'D':
        up = max(0, up - 1)

    if s == 'R':
        right -= 1
    if s == 'L':
        left += 1
    if s == 'D':
        down -= 1
    if s == 'U':
        up += 1

print('YES' if left < sw < right and up < sh < down else 'NO')
