from random import randint
import requests
import random

sammaF = []

antalF = 1
cleanUp = 1
points = 0



url = "https://opentdb.com/api.php?amount=50&difficulty=medium&encode=url3986"
r = requests.get(url)
R = r.json()

Namn = (input("\n     . : FRÅGESPORT : . \n----------------------------\nVälkommen till Vem Kan Allt!\nDu kommer att få 10 stycken kunskapsfågor.\nFår du alla rätt så vinner du\nAbsolut Ingenting!\n\nVi kan börja med ditt namn\n> "))
Namn = Namn.title()

Redo = (input("Dåså "+ Namn +", är du redo?\n> "))
Redo = Redo.title()

if Redo == "Ja":
    print("Då kör vi!\n")

elif Redo == "Nej":
    print("Nähä, men vi kör igång endå!\n")

else:
    print("Jag tolkar det som ett ja så då drar vi igång!\n")

while antalF <11:
    
    l = randint(0,49)

    if l != sammaF:
        sammaF.append(l)

        Fråga = R["results"][l]["question"]
        Rätt = R["results"][l]["correct_answer"]
        Alt = R["results"][l]["incorrect_answers"]

        Fråga = Fråga.replace('%2B','+')
        Fråga = Fråga.replace('%3F','')
        Fråga = Fråga.replace('%2F','')
        Fråga = Fråga.replace('%3A','')
        Fråga = Fråga.replace('%E2','')
        Fråga = Fråga.replace('%88','')
        Fråga = Fråga.replace('%92','')
        Fråga = Fråga.replace('%60','')
        Fråga = Fråga.replace('%20',' ')
        Fråga = Fråga.replace('%21','')    
        Fråga = Fråga.replace('%22','')
        Fråga = Fråga.replace('%23','')
        Fråga = Fråga.replace('%2C','')
        Fråga = Fråga.replace('%24','')
        Fråga = Fråga.replace('%25','')
        Fråga = Fråga.replace('%26','')
        Fråga = Fråga.replace('%27','')
        Fråga = Fråga.replace('%28','')
        Fråga = Fråga.replace('%29','')
        Alt.append(Rätt)
        for items in range(len(Alt)):
            if "%C3" in Alt[items]:
                Alt[items]= Alt[items].replace("%C3","")
        for items in range(len(Alt)):
            if "%B3" in Alt[items]:
                Alt[items]= Alt[items].replace("%B3","")
        for items in range(len(Alt)):
            if "%A9" in Alt[items]:
                Alt[items]= Alt[items].replace("%A9","")
        for items in range(len(Alt)):
            if "%3C" in Alt[items]:
                Alt[items]= Alt[items].replace("%3C","")
        for items in range(len(Alt)):
            if "%3E" in Alt[items]:
                Alt[items]= Alt[items].replace("%3E","")
        for items in range(len(Alt)):
            if "%3A" in Alt[items]:
                Alt[items]= Alt[items].replace("%3A","")
        for items in range(len(Alt)):
            if "%2F" in Alt[items]:
                Alt[items]= Alt[items].replace("%2F","")
        for items in range(len(Alt)):
            if "%2C" in Alt[items]:
                Alt[items]= Alt[items].replace("%2C","")
        for items in range(len(Alt)):
            if "%20" in Alt[items]:
                Alt[items]= Alt[items].replace("%20"," ")
        for items in range(len(Alt)):
            if "%21" in Alt[items]:
                Alt[items]= Alt[items].replace("%21","")
        for items in range(len(Alt)):
            if "%23" in Alt[items]:
                Alt[items]= Alt[items].replace("%23","")
        for items in range(len(Alt)):
            if "%25" in Alt[items]:
                Alt[items]= Alt[items].replace("%25","")   
        for items in range(len(Alt)):
            if "%27" in Alt[items]:
                Alt[items]= Alt[items].replace("%27","")
        for items in range(len(Alt)):
            if "%28" in Alt[items]:
                Alt[items]= Alt[items].replace("%28","")
        for items in range(len(Alt)):
            if "%29" in Alt[items]:
                Alt[items]= Alt[items].replace("%29","")
        for items in range(len(Alt)):
            if "%80" in Alt[items]:
                Alt[items]= Alt[items].replace("%80","")
        for items in range(len(Alt)):
            if "%9D" in Alt[items]:
                Alt[items]= Alt[items].replace("%9D","")
        for items in range(len(Alt)):
            if "%9C" in Alt[items]:
                Alt[items]= Alt[items].replace("%9C","")
        for items in range(len(Alt)):
            if "%3F" in Alt[items]:
                Alt[items]= Alt[items].replace("%3F","")
        for items in range(len(Alt)):
            if "%2C" in Alt[items]:
                Alt[items]= Alt[items].replace("%2C","")
        
        # Alt.append(Rätt)
        random.shuffle(Alt)

        if len(Alt) == 2:
            print(Fråga+"?" + "\n",Alt[0]," - ",Alt[1])

        elif len(Alt) == 3:
            print(Fråga+"?" + "\n",Alt[0]," - ",Alt[1]," - ",Alt[2])
        
        elif len(Alt) == 4:
            print(Fråga+"?" + "\n",Alt[0]," - ",Alt[1]," - ",Alt[2]," - ",Alt[3])

        svartf = (input("> "))
        svartf=svartf.title()

        if svartf == Rätt and antalF<10:
            antalF +=1
            points +=1
            print("Helt rätt, vidare till nästa fråga nummer",antalF,"\n")       
            
        elif svartf != Rätt and antalF<10:
            antalF +=1
            print("Tyvär är det fel, rätt svar är", Rätt+", vi går vidare till fråga nummer",antalF,"\n")
        
        elif svartf == Rätt and antalF == 10:
            points +=1
            print("Helt rätt, det var sista frågan. Här är ditt resultat\n")
            break
        
        elif svartf != Rätt and antalF == 10:
            print("Tyvär är det fel, rätt svar är", Rätt+". Det var sista frågan, här är ditt resultat\n")
            break