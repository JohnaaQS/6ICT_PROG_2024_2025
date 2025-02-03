""" Oefening 1 (   / 8)
Deze oefening bestaat uit 3 niveaus, die je afzonderlijk kan maken. 
Niveau 1 & 2 maken enkel gebruik van de dictionary examen.
Niveau 3 maakt ook gebruik van de lijst deelnemers.

Tip! Als je met een bepaald niveau bezig bent, zet de code van de andere niveaus in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
# Dictionary bevat alle deelnemers die het examen afgelegd hebben, met hun score.
# Sleutel = Naam leerling, Waarde = Score leerling (op 100).
examen = { 
    "Jan": 75,
    "Piet": 59
}

# Lijst bevat alle deelnemers die het examen afleggen.
deelnemers = ["Jan", "Joris", "Piet", "Korneel"]

""" Niveau 1 (   / 2)
Stel een overzicht op met erin iedere leerling die het examen reeds heeft afgelegd (zie examen).
Het overzicht moet eruit zien zoals onderstaand voorbeeld.

De code moet blijven werken ook als de inhoud van examen wijzigt.
Test dit zelf uit door manueel elementen eraan toe te voegen of te verwijderen.

VOORBEELD
---------
Overzicht van examenresultaten...
    - Jan heeft een score van 75/100.
    - Piet heeft een score van 59/100.
"""
for namen, score in examen.items():
    print(f"{namen} heeft een score van {score}/100")


""" Niveau 2 (    / 3)
Print volgende informatie over de dictionary examen:
    - Hoeveel deelnemers het examen reeds hebben afgelegd.
    - De deelnemer die de hoogste score heeft gehaald (en welke score)
    - De gemiddelde score van alle deelnemers samen.

De code moet blijven werken ook als de inhoud van examen wijzigt.
Test dit zelf uit door manueel elementen eraan toe te voegen of te verwijderen.

VOORBEELD
---------
Info over examen...
    - 2 deelnemers heeft het examen reeds afgelegd.
    - Jan heeft het hoogste resultaat (75/100).
    - Het examen heeft een gemiddelde score van 67.0/100.
"""
hoogstescore = -1
totscore = 0
for namen, score in examen.items():
    totscore = score + totscore
    # print(totscore)
    if score > hoogstescore:
         hoogstescore = score
         hoogste_deelnemer = namen
    gem_score = totscore/len(examen)
    
print(f"{len(examen)} leerlingen hebben het examen afgelegd")
print(f"{hoogste_deelnemer} heeft de hoogste score van {hoogstescore}/100")
print(f"de gemiddelde score is {gem_score}")
    



""" Niveau 3 (   / 3)
Overloop de lijst met deelnemers. 

Heeft deze deelnemer het examen reeds afgelegd?
    Print dan: *naam* heeft het examen reeds afgelegd.

Heeft deze deelnemer het examen NIET afgelegd?
    Genereer dan een random score tussen 0 en 100.
    Print dan: *naam* heeft een score van *random*/100 gehaald.
    Voeg tenslotte de deelnemer toe aan de dictionary examen met deze score.

Print op het einde de aangevulde dictionary.
   
VOORBEELD
---------
Examen overlopen...
    - Jan heeft het examen reeds afgelegd.
    - Joris heeft een score van 98/100 gehaald.
    - Piet heeft het examen reeds afgelegd.
    - Korneel heeft een score van 87/100 gehaald.

Eindresultaat examen...
{'Jan': 75, 'Piet': 59, 'Joris': 98, 'Korneel': 87}
"""


# Dictionary bevat alle deelnemers die het examen afgelegd hebben, met hun score.
# Sleutel = Naam leerling, Waarde = Score leerling (op 100).
examen = { 
    "Jan": 75,
    "Piet": 59
}

# Lijst bevat alle deelnemers die het examen afleggen.
deelnemers = ["Jan", "Joris", "Piet", "Korneel"]

import random
for deelnemer in deelnemers:
    if deelnemer in examen:
        print(f"{deelnemer} heeft het examen ingevuld")
    else:
        rand = random.randint(0,100)
        print(f"{deelnemer} heeft het examen nog niet ingevuld")
        print(f"{deelnemer} heeft een {rand}/100")
        if deelnemer not in examen:
            examen[deelnemer] = rand
print(examen)
