import random

top = input("Type a number: ")

if top.isdigit():
    top = int(top)

    if top < 0:
        print("Please enter a number that is greater than 0.")
        quit()
else:
    print("Please type a number next time.")

random_number = random.randint(0, top)
guesses = 0

while True: 
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. \n")
        continue

    if user_guess == random_number:
        print("Hurray! You got it correct.")
        break
    elif user_guess > random_number:
            print("You are above the random number")
    else:
        print("You are below the random number")


print("You got it in ", guesses ," guesses")
