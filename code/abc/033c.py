S = input()
sList = S.split('+')

ans = 0
for s in sList:
    for num in s.split('*'):
        if num == '0':
            break
    else:
        ans += 1

print(ans)