""" Oefening 2 (   / 4)
Onderstaande geneste lijst toont informatie van films en series
Onder de lijst zijn de opgaves van deze oefening te vinden.
"""

media_data = [
    {
        "titel": "The Matrix",
        "geren": "Action",
        "details": {
            "maker": "The Wachowskis",
            "hoofdrollen": ["Keanu Reeves", "Carrie-Anne Moss"]
        },
    },
    {
        "titel": "Breaking Bad",
        "seizoenen": 5,
        "genre": "Crime Drama",
        "details": {
            "maker": "Vince Gilligan",
            "hoofdrollen": ["Bryan Cranston", "Anna Gunn"]
        },
    },
    {
        "titel": "Stranger Things",
        "seizoenen": 4,
        "genre": "Science Fiction",
        "details": {
            "maker": "Duffer Brothers",
            "hoofdrollen": ["Millie Bobby Brown", "Winona Ryder"],
        },
    },
]

""" Niveau 1 (   / 1)
De datastructuur zegt dat Breaking Bad 9 seizoenen had. Dit is fout.
Verander het aantal seizoenen naar 5. Print daarna de dictionary ter controle.
"""
media_data[1]["seizoenen"] = 9
print(media_data[1]["seizoenen"])

""" Niveau 2 (   / 1)
Print onderstaande zin.
Haal zowel 'Stranger Things' als 'Duffer Brothers' uit de datastructuur.

Print: De serie Stranger Things is ontwikkeld door de Duffer Brothers.
"""
media_data[2] #stranger things
serie = (media_data[2]["titel"])
naam = (media_data[2]["details"]["maker"])
print(f" De serie {serie} is ontwikkeld door de {naam}.")


""" Niveau 3 (   / 1)
De sleutel "geren" in "The Matrix" is verkeerd gespeld. Corrigeer dit naar "genre".
Zorg ervoor dat de waarde verbonden aan deze sleutel wel hetzelfde blijft.
Print daarna de dictionary ter controle.
"""
media_data[0]["genre"] = media_data[0]["geren"]
del media_data[0]["geren"]
print(media_data[0])

""" Niveau 4 (    / 1)
Print een overzicht van iedere film/serie in de datastructuur.
Dit overzicht bevat de naam van de film/serie en de eerste hoofdrolspelers.
De print moet er als volgt uitzien.

Overzicht films:
    - The Matrix met als hoofdrolspeler Keanu Reeves.
    - Breaking Bad met als hoofdrolspeler Bryan Cranston.
    - Stranger Things met als hoofdrolspeler Millie Bobby Brown.

De code moet blijven werken ook als de inhoud van media_info wijzigt.
"""
for index, series in enumerate(media_data): 
    print(index)
    print(media_data[index]["titel"])
    print(media_data[index]["details"]["hoofdrollen"][0])
    print(f"{media_data[index]["titel"]} met als hoofdrolspeler {media_data[index]["details"]["hoofdrollen"][0]} ")
    
