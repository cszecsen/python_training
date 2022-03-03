number_of_numbers = int(input("Hány számot szeretne megadni?"))

sum = 0
i = 0
while i < number_of_numbers:
    k = int(input("Adja meg a számot"))
    if k % 2 ==0:
        sum += k
    i +=1
print("A páros számok összege:" + str(sum))
