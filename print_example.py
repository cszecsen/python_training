# print("alma", end="")
# print("körte", end="")

# Hozz létre

def table():
    for i in range(1,11):
        for j in range(1,11):
            print(str(i*j)+ " ", end="")
        print("\n")

# table()

def digits(number):
    while number > 10:
        remainder = number % 10
        print(remainder)
        number = number // 10
    print(number)

number = 1865
digits(number)