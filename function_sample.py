# Hozz létre egy is_even nevű függvényt
# amely True-t ad vissza, ha paraméterként megadott érték páros
# egyéb esetben False-t adjon vissza

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(5))
print(is_even(6))

# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# # és összegzi a benne szereplő negatív számokat, és azzal tér vissza

def sum_negatives(list_of_numbers):
    negative_sum = 0
    for number in list_of_numbers:
        if number < 0:
            negative_sum += number
    return negative_sum


numbers = [-5, 2, -1, 3, -10]
print(sum_negatives(numbers))


# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával

def to_minutes(number_of_hours):
    return number_of_hours *60


hours = 4
print("A percek száma: ", to_minutes(hours))


# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza

def input_number():
    number = int(input("Adjon meg egy számot!"))
    return number

n = input_number()
print(n)

# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki

def annotate_every_even_number(number_list):
    index = 1
    for number in number_list:
        if index % 2 != 0:
            print(number)
        else:
            print(" " + str(number))
        index += 1


numbers = [1, 2, 3, 4, 5, 6]
annotate_every_even_number(numbers)


# Írj egy concatenate_shorts függvényt, mely paraméterül kap szavak listáját
# és csak a 3 karakternél rövidebb szavakat fűzze össze egy stringbe,
# és ezt adja vissza

def concatenate_shorts(list_of_words):
    text = ""
    for word in list_of_words:
        if len(word) < 3:
            text += word
    return text

words = ["alma", "kő", "piros", "egy", "tő"]
print(concatenate_shorts(words))