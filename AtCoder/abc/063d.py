N, A, B = map(int, input().split())
HP = []

for _ in range(N):
    HP.append(int(input()))

left = 0
right = max(HP)

def canKill(count):
    ness = 0
    for hp in HP:
        ness += max(-(-(hp - B * count) // (A - B)), 0)
    if ness <= count:
        return True
    return False

while right - left > 1:
    middle = left + (right - left) // 2
    if canKill(middle):
        right = middle
    else:
        left = middle

print(right)