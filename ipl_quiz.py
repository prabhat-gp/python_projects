print("Welcome to my IPL quiz!  ")

playing = input("Do you wanna play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play ")
score = 0

ques_1 = input("What is AB's highest score in IPL? ")
if ques_1.lower() == "133":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_2 = input("How many finals has RCB reached in IPL? ")
if ques_2.lower() == "3":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_3 = input("Against which team of IPL, RCB is unbeaten? ")
if ques_3.lower() ==  "gl":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_4 = input("Against which team, VK got out on 99? ")
if ques_4.lower() == "dd":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_5 = input("Which player has played RCB twice? ")
if ques_5.lower() == "dk" or "hp":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_6 = input("Distance of the longest six hit by Gayle: ")
if ques_6 == "119":
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

ques_7 = input("Which team has the best fans? ")
if ques_7.lower() == "rcb" :
    print("Correct \n")
    score +=1
else:
    print("Incorrect! \n")

print("You have scored " + str(score) + "/7 points" )
print("You have scored ", score  ,"/ 7 points" )
print("You got " + str(round((score / 7) * 100)) + "%.")
