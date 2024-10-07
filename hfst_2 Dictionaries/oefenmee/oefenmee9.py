recept = { # Sleutel is ingrediënt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
while True: 
    aantal_man = int(input("met hoeveel man eet je? "))
    print(f"het recept voor {aantal_man} man is")
    for sleutel , waarde in recept.items():
     waarde = int(waarde/4 * aantal_man)
     print(f"- {sleutel}: {waarde} gr.")
     

     
    
    