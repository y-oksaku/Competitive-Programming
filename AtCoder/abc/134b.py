N, D = map(int, input().split())

def ceil(a,b) :
    return (a + b - 1) // b

print(ceil(N, 2*D + 1))