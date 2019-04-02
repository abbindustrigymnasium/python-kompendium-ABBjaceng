namn = (input("Ange ditt namn: "))
ålder = (input("Ange din ålder: "))

if ålder == "0":
    totsömn = "15"
elif ålder == "1":
    totsömn = "14"
elif ålder == "2":
    totsömn = "13"
elif ålder == "3":
    totsömn = "12"
elif ålder == "4":
    totsömn = "11,5"
elif ålder == "5" or ålder == "6":
    totsömn = "11"
elif ålder == "7":
    totsömn = "10,5"
elif ålder == "8" or ålder == "9" or ålder == "10":
    totsömn = "10"
elif ålder == "11":
    totsömn = "9,5"
elif ålder == "12"or ålder == "13" or ålder == "14" or ålder == "15":
    totsömn = "9"
elif ålder == "16":
    totsömn = "9,5"
else:
    totsömn = "8" 

print ("-----\nHallå " + namn + "! Enligt Vårdguidens\nrekommendationer behöver individer i din ålder (" + ålder + " år)\nsova minst " + totsömn + " timmar per natt.")