import random


print("\n. : THE HIGHER LOWER GAME : .\n------------------------------\nWelcome to The Higher Lower\nGame! I will randomise a\nnumber between  0  and  99.\nCan you guess it?\n------------------------------")
guess=int(input("Your guess > "))
nummer = int(random.randint(0,99))
chans=1

while guess != nummer:
    if guess > nummer:
        print("LOWER")
        chans+=1
    else:
        print("HIGHER")
        chans+=1
    
    guess=int(input("Try again > "))

print("------------------------------\n",nummer,"is correct!\nIt only took you",chans,"guess(es).\nGood job!\n")
