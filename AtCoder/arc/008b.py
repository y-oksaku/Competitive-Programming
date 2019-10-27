from collections import Counter

N, M = map(int, input().split())
Name = input()
Kit = input()

cntName = Counter(Name)
cntKit = Counter(Kit)

ans = 0
for w, cnt in cntName.items():
    if cntKit[w] == 0:
        print('-1')
        exit()
    nessKit = (cnt + cntKit[w] - 1) // cntKit[w]
    ans = max(ans, nessKit)

print(ans)