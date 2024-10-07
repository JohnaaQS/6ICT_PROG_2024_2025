#dictonary fruit
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
 
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
fruit = "banaan"
print( fruitmand[fruit] )
print(fruitmand)

#nieuwe fruit toevoegen 
nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand[nieuw_fruit] = nieuw_aantal
print(fruitmand)

nieuw_aantalBananen = int(input("hoeveel wil je er?: "))
fruitmand["banaan"] = nieuw_aantalBananen
print(fruitmand)

soortfruit = input("welke fruit wil je eten?: ")
if soortfruit in fruitmand:
    aantalfruit = int(input("Hoeveel stuks wil je?: "))
    fruitmand[soortfruit] = aantalfruit
    print(fruitmand)
    
else:
    print("gegeven fruitstuk is er niet. ")

wegfruit = input("welke fruisoort moet weg?: ")
if wegfruit in fruitmand:
    fruitmand.pop(wegfruit)
    print(fruitmand)
