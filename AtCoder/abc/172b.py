S = input()
T = input()

print(len([0 for s, t in zip(S, T) if s != t]))
