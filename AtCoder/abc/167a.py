import string

S = input()
T = input()

for a in string.ascii_lowercase:
    if S + a == T:
        print('Yes')
        exit()

print('No')