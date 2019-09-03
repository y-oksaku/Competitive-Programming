N = int(input())
R = input()

score = 0
for r in R:
    if r == 'A':
        score += 4
    elif r == 'B':
        score += 3
    elif r == 'C':
        score += 2
    elif r == 'D':
        score += 1

print(score / N)