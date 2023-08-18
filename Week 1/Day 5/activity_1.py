def film_check(name):
    if name[2].lower() == "ghostbusters":
        print("Yey it's ghostbusters.")
    else:
        print("booo, we want ghostbusters.")

films = [
    "film 1",
    "film 2",
    "film 4", 
    "Ghostbusters",
]

for i in films:
    print(i)

film_check(films)