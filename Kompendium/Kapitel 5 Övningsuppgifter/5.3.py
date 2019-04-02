Land = (input("Välj ett land: "))
Land=Land.title()

if Land == "Sverige" or Land == "Norge" or Land == "Island" or Land == "Finland" or Land == "Danmark":
    print(Land,"är en del av Norden")

elif Land == "England" or Land == "Nordirland" or Land == "Skottland" or Land == "Wales":
    print(Land,"är en del av Storbritanien")

else:
    print(Land,"tillhör inte Norden eller Storbritanien")