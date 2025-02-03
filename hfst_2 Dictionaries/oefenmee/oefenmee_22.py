lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]
sumlijst = 0
aantal = 0
for index_hoofd, sublijst in enumerate(lijst):
 aantal += len(sublijst)
 sumlijst += sum(sublijst)
 print(f"{index_hoofd}: {sumlijst}")
 

print(sumlijst)
gemiddelde = sumlijst / aantal
print(gemiddelde)
