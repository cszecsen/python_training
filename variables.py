#Literál - érték

print(5) # Egész szám
print(100_000)

print(3.14)  # Lebegőpontos literál

print("Hello World")
print('Hello World')

employee_name = "John Doe"
print(employee_name)

age = 30
print(age)
age = 31
print(age)

color_of_eye = "blue"
print(color_of_eye)


color_of_eye_of_john = color_of_eye
print(color_of_eye_of_john)

print(type(5)) # int = integer
print(type(3.14)) # float - lebegőpontos szám
print(type(employee_name)) # str = string - karakterlánc

age = 32
print(type)

age = "harminckettő"
print(age)
print(type(age))

# literálok, változóknak - van típusa - Python típusos nyelv
# változóknál a típus változhat - dinamikusan típusos nyelv

#type hint
salary: int = 200
print(salary)
salary = "kétszáz"
print(salary)

