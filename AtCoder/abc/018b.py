S = input()
N = int(input())

for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    S = S[:l] + S[l: r][::-1] + S[r:]

print(S)
