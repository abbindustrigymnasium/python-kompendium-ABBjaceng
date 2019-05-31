from random import randint
import requests
import random

sammaF = []     #en array som ser till att inte samma fråga ställs flera gånger

antalF = 1      #hur många frågor koden har stält
points = 0      #hur många poäng spelaren har

url = "https://opentdb.com/api.php?amount=50&difficulty=medium"     #genom att ta bort allt efter medium så behövde jag inte använda lika många replace
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

while antalF <11:       #det går att ändra hur många frågor man vill ha genom att ändra detta värde
    
    l = randint(0,49)

    if l != sammaF:     #här är funktionen som gör så att inte samma fråga ställs flera gånger
        sammaF.append(l)

        Fråga = R["results"][l]["question"]
        Rätt = R["results"][l]["correct_answer"]
        Alt = R["results"][l]["incorrect_answers"]

        Fråga = Fråga.replace('&quot;','')
        Fråga = Fråga.replace('&ldquo;','')
        Fråga = Fråga.replace('&rdquo;','')
        Fråga = Fråga.replace('&#039','')
                                                    #det krävs fortfarande några replase för att få koden att se bra ut
        for items in range(len(Alt)):
            if "&quot;" in Alt[items]:
                Alt[items]= Alt[items].replace("&quot;","")
        for items in range(len(Alt)):
            if "&ldquo;" in Alt[items]:
                Alt[items]= Alt[items].replace("&ldquo;","")
        for items in range(len(Alt)):
            if "&rdquo;" in Alt[items]:
                Alt[items]= Alt[items].replace("&rdquo;","")
        for items in range(len(Alt)):
            if "&#039" in Alt[items]:
                Alt[items]= Alt[items].replace("&#039","")
        
        Alt.append(Rätt)
        random.shuffle(Alt)     #blandar alternativen i arrayen så att rätt svar inte är på samma plats varje gång

        if len(Alt) == 2:
            print(Fråga + "\n",Alt[0]," - ",Alt[1])

        elif len(Alt) == 3:
            print(Fråga + "\n",Alt[0]," - ",Alt[1]," - ",Alt[2])        #ibland är det färre än fyra altenaativ. dessa if/elif satser gör att den bara skriver ut rätt antal alternativ
        
        elif len(Alt) == 4:
            print(Fråga + "\n",Alt[0]," - ",Alt[1]," - ",Alt[2]," - ",Alt[3])

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
            print("Helt rätt, det var sista frågan. Här är ditt resultat:\nAv 10 möjliga fick du",points)
            if points < 6:
                print("Du kan bättre.\n")
            else:
                print("Bra jobbat!\n")
            break
        
        elif svartf != Rätt and antalF == 10:
            print("Tyvär är det fel, rätt svar är", Rätt+". Det var sista frågan, här är ditt resultat\nAv 10 möjliga fick du",points)
            if points < 6:
                print("Du kan bättre.\n")
            else:
                print("Bra jobbat!\n")
            break