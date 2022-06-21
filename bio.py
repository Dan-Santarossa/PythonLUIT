name = input("What is your name? ")
colour = input("What is your favourite colour? ")
age = int(input("How old are you? "))

#print(name, end=" ")
#print("is " + str(age) + " years old", end=" ")
#print("and loves the colour " + colour + ".", end=" ")

print(name, 'is', age, 'years old and loves the colour', colour, ".", sep=" ")