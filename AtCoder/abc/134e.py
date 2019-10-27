import bisect

N = int(input())
A = []

a = int(input())

val = [-a]
length = 1

for _ in range(N - 1) :
    a = int(input())
    a *= -1
    i = 0

    index = bisect.bisect_right(val, a)
    if index >= length :
        val.append(a)
        length += 1
    else :
        val[index] = a

print(length)