K = int(input())

even = 0
odd = 0

for k in range(1, K + 1):
    if k % 2 == 0:
        even += 1
    else:
        odd += 1

print(even * odd)