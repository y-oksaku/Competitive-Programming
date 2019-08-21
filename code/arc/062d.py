S = input()

count = 0
for s in S :
    if s == 'p' :
        count += 1

ans = -count + len(S) // 2
print(ans)