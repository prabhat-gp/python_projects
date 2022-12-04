name = input("Enter your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has to and end and you can go either left or right. Which way would you like to go? "
    ).lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim across? Type walk to walk around and swim to swim around: ").lower()

    if answer == "swim":
            print("You swam across and was eaten by an alligator.")
    elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
    else: 
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()
        if answer == "yes":
            print("Hurray! You talked to the stranger and they gave you the gold and you won the adventure.")
        elif answer == "no":
            print("You ignored the stranger and you lost an opportunity to win the gold. You lose.")
        else:
            print("Not a valid option. You lose.")    
    else: 
        print("Not a valid option. You lose.")
else: 
    print("Not a valid option. You lose.")

print("Thank you for trying", name)