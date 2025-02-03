# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}


for speler, info in spelinfo.items():
    print(f"Informatie voor {speler}:")
    print(f"Naam: {info['naam']}")
    print(f"Positie: x={info['positie']['x']}, y={info['positie']['y']}")
    print(f"Wapen: {info['inventaris']['wapen']}")
    print(f"Goud: {info['inventaris']['goud']}")
    print("-" * 20)
