steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}

while True: 
 naam = input("geef je stad op: ")
 if naam == "stop":
     break
 if naam in steden_temp:
     temp = steden_temp[naam]
     print(f"in {naam} is het {temp} °C")
 else: 
    print("deze stad bevind zich niet in de lijst.")
