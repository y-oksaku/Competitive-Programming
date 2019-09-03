E = input()
B = input()
L = input()

for e in E:
    L = L.replace(e, '', 1)

if len(L) == 0:
    print(1)
elif len(L) == 1:
    if L == B:
        print(2)
    else:
        print(3)
elif len(L) == 2:
    print(4)
elif len(L) == 3:
    print(5)
else:
    print(0)