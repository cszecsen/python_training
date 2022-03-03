# Kérjük be a felhasználótól a nevét, ha üres, akkor  írjuk ki, hogy nem lehet üres értéket megadni és kérjük be még egyszer
# Ha nem üres, írjuk ki, hogy köszönöm

name = ""
while name == "":
    name = input("Add meg a neved: ")
    if name == "":
        print("Nem adhatsz meg üres értéket!")

print("Köszönöm!")