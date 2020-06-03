A = list(range(1, int(input()) + 1))
A.sort(key=lambda a: (a & -a).bit_length())
print(A[-1])
