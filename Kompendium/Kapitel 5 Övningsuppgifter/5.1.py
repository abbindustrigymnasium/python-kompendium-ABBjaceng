kön = str(input("Vilket kön har du? - "))
hårfärg = str(input("Vilken hårfärg har du? - "))
ögonfärg = str(input("Vilken ögonfärg har du? - "))

if kön == "man":
    if hårfärg == "brun":
        if ögonfärg == "brun":
            print("Du liknar Daniel Radcliffe")

elif kön == "man":
    if hårfärg == "röd":
        if ögonfärg == "blå":
            print("Du liknar Rupert Grint")

elif kön == "kvinna":
    if hårfärg == "brun":
        if ögonfärg == "brun":
            print("Du liknar Emma Watson och Selena Gomez")

else:
    print("Du liknar ingen")