import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

with open("6ICT_PROG_2024_2025\hfst_4 API\oefenmee/advicesclip.json", "w",) as fp:
    json.dump(response_json, fp)
    print("json gedumpt!") 

print("Hier is wat wijsheid over API's...")
print(response_json['slips'][0]['advice'])
