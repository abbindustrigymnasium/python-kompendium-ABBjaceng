tal = 0
summa = 0
mängd = []

while tal < 1000001:     
    mängd.append(tal)
    summa = summa + tal
    tal+=1
else:
    for nummer in mängd:
        print(nummer)
        
print("Total summan är", summa)