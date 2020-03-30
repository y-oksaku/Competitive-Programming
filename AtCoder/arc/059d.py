s = input()

for i in range(len(s) - 1):
    if len(set(s[i: i + 2])) == 1:
        print(i + 1, i + 2)
        exit()
for i in range(len(s) - 2):
    if len(set(s[i: i + 3])) <= 2:
        print(i + 1, i + 3)
        exit()

print('-1 -1')