a, b = map(lambda a: 1 if a == 'H' else -1, input().split())
print('H' if a * b == 1 else 'D')