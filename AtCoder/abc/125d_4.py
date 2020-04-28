N = int(input())
A = list(map(int, input().split()))
M = len([0 for a in A if a < 0])

if A.count(0) > 0 or M % 2 == 0:
    print(sum(abs(a) for a in A))
    exit()

print(sum(abs(a) for a in A) - min(abs(a) for a in A) * 2)
