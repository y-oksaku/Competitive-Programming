N = int(input())

count = {
    'M' : 0,
    'A' : 0,
    'R' : 0,
    'C' : 0,
    'H' : 0,
}

for _ in range(N):
    s = input()
    if s[0] in count:
        count[s[0]] += 1

ans = 0
count = list(count.items())
for i in range(len(count)):
    for j in range(i + 1, len(count)):
        for k in range(j + 1, len(count)):
            ans += count[i][1] * count[j][1] * count[k][1]

print(ans)