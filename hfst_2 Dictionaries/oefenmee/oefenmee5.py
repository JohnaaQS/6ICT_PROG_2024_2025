films = ["godfather", "avatar", "oppenheimer"]
scores = [9, 3, 7.5]

filmscores = {}
for index, film in enumerate(films):
    sleutel = film
    waarde = scores[index]
    filmscores[sleutel] = waarde

print(filmscores)
