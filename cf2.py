t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    
    suneet_wins = 0
    
    if a1 > b1:
        suneet_wins += 1
    if a1 > b2:
        suneet_wins += 1
    if a2 > b1:
        suneet_wins += 1
    if a2 > b2:
        suneet_wins += 1
    
    if suneet_wins >= 3:
        print(4)
    elif suneet_wins == 2:
        print(2)
    else:
        print(0)
