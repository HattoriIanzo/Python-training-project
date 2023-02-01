print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 42

kick = input("Type your number: ")

number = int(kick)

print("You typed", kick)

if secret_number == number:
    print("You got it!")
else:
    print("You missed!")
