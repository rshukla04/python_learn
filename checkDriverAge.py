def checkDriverAge(age):
    age = 0
    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


print(checkDriverAge(92))