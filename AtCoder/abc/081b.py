input()
print(min(map(lambda a: int(a) & (-int(a)), input().split())).bit_length() - 1)