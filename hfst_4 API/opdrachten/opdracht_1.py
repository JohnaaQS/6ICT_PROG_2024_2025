""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""
import requests, json
url = 	"https://api.adviceslip.com/advice/search/teeth"
response_json = requests.get(url).json()

with open("6ICT_PROG_2024_2025\hfst_4 API\opdrachten/opdr1.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")