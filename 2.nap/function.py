# Függvény definíciója
def print_employee_data(name, age):
    """Ez a függvény kiírja az alkalmazott nevét és életkorát"""
    # DRY = don't repeat yourself
    print("Az alkalmazott neve: ", name)
    print("Az alkalmazott életkora: ", age)
    # függvény végén a paraméterek törlődnek, nincs többé name és age


def print_dog_name(name):
    print("A kutya neve: ", name)


def print_sum(a, b):
    print("A két szám összege:", a+b)


print_sum(3, 5)
print_employee_data("John", 10)  # Függvény hívás
# átmásolás sorrendben történik: sorrendi kötés
print_employee_data("Jack", 20)
print_employee_data("Jane", 30)
print_dog_name("Morzsi")

# Írjatok egy sum_list függvényt, ami paraméterül kap egy listát
# és kiírja a konzolra, a listában szereplő számok összegét

def sum_list(input_data):
    sum = 0
    for number in input_data:
        sum += number
    print("Az összeg: ", sum)


numbers = [1, 2, 5, 8]
sum_list(numbers)