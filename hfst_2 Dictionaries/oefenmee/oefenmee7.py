gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}



while True: 
 naam = input("geef je naam op: ")
 if naam == "stop":
     break
 if naam in gasten:
     functie = gasten[naam]
     print(f"welkom {naam} je hebt de functie {functie}")
     gasten.pop(naam)
     print(gasten)
 else:
     print("Gast bestaat niet")
    