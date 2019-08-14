from collections import Counter

N = int(input())
A = set(list(map(int, input().split())))

# カードは1 or 2枚まで減らせる
# Nは奇数なので，1枚のカードは奇数種
# 全体で奇数種のとき，2枚のカードは偶数種
# 偶数種のとき，奇数種
# 2枚のカードはペアで1枚ずつにできる

ans = len(A) - (0 if len(A) % 2 == 1 else 1)
print(ans)
