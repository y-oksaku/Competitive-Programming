A, B, C, D = map(int, input().split())
print('Yes' if max(A, C) <= min(B, D) else 'No')
