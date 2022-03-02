print(5 * 6)
print(5 + 6)
print(3 / 2)
print(3 - 2)

print(5 * 6 + 12)
print(1 + 2 * 3)

print((1 + 2) * 3)

print("alma" + "körte") # konkatenálás

# Mi van, ha össze akarsz adni egy str-et és egy int-et?

# print("öt" + 5) # TypeError: can only concatenate str (not "int") to str

# Mi van fordítva?

# print(5 + "öt") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Mi van, ha egy stringből ki akarsz vonni egy másikat?

# print("tíz" - "kettő") # TypeError: unsupported operand type(s) for -: 'str' and 'str'

# Mi van ha egy stringet megszorzol egy másik stringgel?

# print("tíz" * "kettő") # TypeError: can't multiply sequence by non-int of type 'str'

# Mi van, ha egy stringet megszorzol egy int-tel?

print("tíz" * 5)

result = 6 * 5 + 2
print(result)

number_of_apples_per_basket = 5
number_of_baskets = 3
number_of_all_apples = number_of_apples_per_basket * number_of_baskets
print(number_of_all_apples)

name = "John Doe"
message = "A name változó tipusa: " + str(type(name))
print(message)

print("Az almak szama: " + str(5))

# kifejezések végrehajtása: kiértékelés
length_of_hello = len("hello")
print(length_of_hello)

# hozzatok létre egy változót, hogy órák száma, hours
# hozzatok létre egy másik változót, neve: minutes, tartalmazza, hogy hány perc - előző változó szorzása 60-nal

hours = 3
minutes = hours * 60
print(str(hours) + " óra az " + str(minutes) + " perc")

message = str(hours)
message = message + " óra az "
message = message + str(minutes)
message = message + " perc"

print(message)

word = "húezdenagyonhosszúszómintahogyafeladatkérte"

print("A " + word + " pontosan " + str(len(word)) +" karakter hosszú.")

fruit = "alma"
print('gyumolcs: "' + fruit + '"')
print("gyumolcs: \"" + fruit + "\"")

# print(FRUIT) Python case-sensitive


