A, B = map(int, input().split())

ans = float('inf')
for ten in range(-10, 11):
    for five in range(-10, 10):
        one = B - A - ten * 10 - five * 5
        ans = min(ans, abs(ten) + abs(five) + abs(one))

print(ans)
