from collections import Counter

print('Yes' if all(n % 2 == 0 for n in Counter(list(input())).values()) else 'No')
