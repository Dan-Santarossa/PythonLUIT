name = input("What is your name? ")

if len(name) >= 6:
    print("your name is long")
elif len(name) == 5:
    print("your name is 5 characters")
elif len(name) >= 4:
    print("your name is 4 or more characters")
else:
    print("your name is short")