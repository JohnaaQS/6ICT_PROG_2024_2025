talen =    ["Python", "Java", "Javascript", "C#", "PHP", "Overig"]
aandelen = [29.48   , 17.18 , 9.14        , 6.94, 6.49 , 9.93]
taal_aandeel = {} # Zet lege dict klaar.

for index, taal in enumerate(talen):
 waarde = aandelen[index] 
 taal_aandeel[taal] = waarde
 
print(taal_aandeel)
