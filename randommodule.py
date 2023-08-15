import random
numberofstreaks = 0
containsstreak = False
coinflip = []
streak = 0

for experimentnumber in range(10000):

    for i in range(100):
        coinflip.append(random.randint(0,1))

    for i in range(len(coinflip)):
        if i == 0 :
            pass
        
        elif coinflip[i] == coinflip[i-1]:
            streak += 1

        else:
            streak = 0

        if streak == 6:
            containsstreak = True

    if containsstreak:
        numberofstreaks += 1

    coinflip = []
    streak = 0
    containsstreak = False

print('chances of streak :', numberofstreaks/100)