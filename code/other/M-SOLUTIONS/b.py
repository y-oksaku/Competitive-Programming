s = input()

count = 0
for i in range(len(s)) :
    if s[i] == 'o' :
        count += 1

if count + 15 - len(s) >= 8 :
    print('YES')
else :
    print('NO')