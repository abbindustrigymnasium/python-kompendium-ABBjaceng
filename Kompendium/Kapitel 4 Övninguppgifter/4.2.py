tal = 1
summa = 0
mängd = []

while tal < 501:     
    mängd.append(tal)
    summa = summa + tal
    tal+=2
else:
    for nummer in mängd:
        print(nummer)
        
print("Total summan är", summa)