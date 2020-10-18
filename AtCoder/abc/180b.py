N = int(input())
A = list(map(int, input().split()))

print(
    sum(map(abs, A)),
    sum(map(lambda a: a**2, A))**0.5,
    max(map(abs, A)),
    sep='\n'
)
