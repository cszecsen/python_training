print("Gondolj egy számra!")
min = 1
max = 10
answer = ""

while answer != "e":
    guess = (min + max) // 2
    print("A tippem", guess)
    answer = input("k/e/n")
    if answer == "k":
        max = guess - 1
    elif answer == "n"


# min_number = int(input("Add meg az alsó határt!"))
# max_number = int(input("Add meg a felső határt!"))
#
# print("Gondolj egy számra " + str(min_number) + " és " + str(max_number) +" között!")
#
# answer = "x"
#
# while answer != "igen":
#     guess = int((max_number + min_number) / 2)
#     answer = input("A kigondolt szám:" + str(guess) + " ? (igen/kisebb/nagyobb)")
#     if answer == "kisebb":
#         max_number = guess
#     if answer == "nagyobb":
#         min_number = guess
#
# print("A gondolt szám:" + str(guess))




