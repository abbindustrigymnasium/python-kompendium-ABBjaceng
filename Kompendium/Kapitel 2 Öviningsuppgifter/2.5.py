import math
print(". : KORVKOLLEN 1.0.1 : .")
print("---------------------------")
print("Hur många elever vill ha...")

vanliga2 = int(input("2 vanliga korvar      >  "))
vanliga3 = int(input("3 vanliga korvar      >  "))
vego2 = int(input("2 vegetariska korvar  >  "))
vego3 = int(input("2 vegetariska korvar  >  "))

sumvanligkorv = (vanliga2 * 2)+(vanliga3 * 3)
sumvegokorv = (vego2 * 2)+(vego3 * 3)
sumdryck = vanliga2+vanliga3+vego2+vego3

korvpaket = sumvanligkorv/8
vegopaket = sumvegokorv/4

korvpaket = math.ceil(korvpaket)
vegopaket = math.ceil(vegopaket)

kostnadkorv = korvpaket*20.95
kostnadvego = vegopaket*34.95
kostnaddryck = sumdryck*13.95

totkostnad = kostnaddryck+kostnadkorv+kostnadvego

totalkostnad = round(totkostnad)

print("---------------------------")
print("-  INKÖPSLISTA             -")
print("---------------------------")
print("|  Vanlig korv:    ",korvpaket," förpakningar") 
print("|  Vegansk korv:   ",vegopaket," förpakningar") 
print("|  Dryck:          ",sumdryck," drycker")
print("---------------------------")
print("|  ",totkostnad," SEK")
print("---------------------------")
