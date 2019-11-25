S = input()
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i, w in enumerate(week):
    if S == w:
        print(7 - i)