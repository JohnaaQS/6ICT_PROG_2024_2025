lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for index, rij in enumerate(lijst_2D):
    if index == 0 or index == 2:  
        for j, element in enumerate(rij):
            print(f"{index},{j}: {element}")