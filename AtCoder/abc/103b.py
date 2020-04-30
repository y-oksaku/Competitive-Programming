S = input()
T = input()

def can():
    for i in range(len(S)):
        U = S[i:] + S[:i]
        if U == T:
            return True
    return False

print('Yes' if can() else 'No')
