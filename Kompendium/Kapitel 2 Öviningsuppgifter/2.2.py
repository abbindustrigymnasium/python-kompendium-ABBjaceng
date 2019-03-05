print("Skriv ett decimaltal")
flyttal = float(input(">> ")) + 0.5 #Jag lägger till 0,5 för att den ska avrunda till det närmaste heltal
heltal = int(flyttal) 
print("Ditt tal blir " + str(heltal))
