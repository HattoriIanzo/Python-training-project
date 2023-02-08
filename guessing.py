print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 42

kick = input("Type your number: ")

number = int(kick)

Right    = number == secret_number
morethan = number > secret_number
lessthan = number < secret_number

print("You typed", kick)

if (Right):
    print("You got it!")
else:
    if (morethan):
        print("You missed! You guessed more than the secret number")
    elif(lessthan):
        print("You missed! You guessed less than the secret number")
print("Game Over!")
print("I'm hungry")
