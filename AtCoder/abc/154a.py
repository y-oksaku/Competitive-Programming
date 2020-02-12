S, T = input().split()
N = {s : int(n) for s, n in zip((S, T), input().split())}
N[input()] -= 1
print(N[S], N[T])
