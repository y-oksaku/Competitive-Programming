from string import ascii_lowercase

S = input()
D = dict()

for s in S:
    D[s] = True

for s in ascii_lowercase:
    if not s in D:
        print(s)
        exit()
print('None')
