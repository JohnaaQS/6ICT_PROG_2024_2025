import requests, json

url = "https://v2.jokeapi.dev/joke/Christmas?amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.

with open("6ICT_PROG_2024_2025\hfst_4 API\oefenmee/fa2.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
    
for joke in response_json['jokes']:
    # Bepaal of de grap uit 1 of 2 delen bestaat.
    if ("joke" in joke):
        print(joke["joke"])     # De grap
    else:
        print(joke["setup"])    # De setup
        print(joke["delivery"]) # De punchline
     

