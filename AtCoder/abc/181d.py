from collections import Counter
S = Counter(list(input()))

def canMake(i):
    cnt = Counter(list(str(i)))
    for s, c in cnt.items():
        if S[s] < c:
            return False
    return True

for i in range(100, 1000):
    if i % 2 == 1:
        continue
    if (i // 2) % 100 % 4 == 0:
        if canMake(i):
            print('Yes')
            exit()

for i in range(100):
    if i % 8 == 0 and Counter(list(str(i))) == S:
        print('Yes')
        exit()

print('No')
