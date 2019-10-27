from collections import Counter

N = int(input())

charList = Counter(input())

for _ in range(N - 1):
    countS = Counter(input())
    for char, num in charList.items():
        if char in countS:
            charList[char] = min(num, countS[char])
        else:
            charList[char] = 0

intersectChar = []
for char, num in charList.items():
    for i in range(num):
        intersectChar.append(char)

intersectChar.sort()
print(''.join(intersectChar))