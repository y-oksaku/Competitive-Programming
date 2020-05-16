A = int(input().replace(' ', ''))

for i in range(A):
    if i**2 == A:
        print('Yes')
        exit()
print('No')
