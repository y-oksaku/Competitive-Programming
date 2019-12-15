N = input()

for i in range(10):
    if ''.join([str(i)] * 3) in N:
        print('Yes')
        break
else:
    print('No')