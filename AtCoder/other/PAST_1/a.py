import string

S = input()

for s in string.ascii_lowercase:
    if S.count(s) > 0:
        print('error')
        exit()

print(int(S) * 2)
