N = int(input())

# 最初の符号
print(0, flush=True)
first = input()

if first == 'Vacant':
    exit()

if first == 'Male':
    first = 1
else:
    first = -1

notHas = 1
has = N - 1

while has - notHas > 1:
    mid = (notHas + has) // 2
    print(mid, flush=True)
    ret = input()

    if ret == 'Vacant':
        exit()

    if ret == 'Male':
        ret = 1
    else:
        ret = -1

    trueValue = first * (-1)**(mid % 2)
    if ret == trueValue:
        notHas = mid
    else:
        has = mid

print(notHas, flush=True)
ret = input()

if ret == 'Vacant':
    exit()

print(has, flush=True)
input()
exit()