sum = int(input("Adj meg egy számot! "))

if sum == 0:
    print("A megadott szám nulla!")
else:
    while sum != 0:
        number = int(input("Add meg a következő számot! "))
        sum += number
        if sum == 0:
            print("A részösszeg nulla. A program leáll.")
        else:
            print("Részösszeg: " + str(sum))