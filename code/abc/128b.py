N = int(input())

A = []

# 出力を受け取る
for i in range(N):
    Si , Pi = input().split()
    Pi = int(Pi) # 型変換

    A.append([i,Si,Pi])

# リストにアクセス
second = lambda A : A[1]
third = lambda A : A[2]

# ソート
A.sort(key=third,reverse=True)
A.sort(key=second)

for target in A:
    print(target[0] + 1)