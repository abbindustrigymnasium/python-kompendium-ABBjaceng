tal = int(input("Ange multiplikationstabell > "))
multi = 1
beg = 4

while multi < beg:
    print(tal*multi)
    multi += 1
    if multi == beg:
        svar = (input("fortsätt? > "))
        if svar == "ja":
            beg += 3