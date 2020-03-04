A = [int(input()) for _ in range(3)]
B = {a : i for i, a in enumerate(sorted(A, reverse=True), start=1)}

for a in A:
    print(B[a])
