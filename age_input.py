year = int(input("Adja meg a születési évét!"))

minimum_year = 1900
actual_year = 2022
if year < minimum_year or year > actual_year:
    print("Helytelen születési év!")
else:
    print("Az életkorod: " + str(actual_year-year))