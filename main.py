import random

computerMove = random.choice([-1,0,1])

youstr = input("Enter your choice press s,g or w:")
youDict = {"s":1, "w": -1, "g": 0}

reverseDict = {1:"snake",-1:"water",0:"gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computerMove]}")


if(computerMove == you):
    print("Its a Draw")

else:
    if(computerMove == -1 and you == 1):
        print("You Win!")

    elif(computerMove == -1 and you == 0):
        print("You lose!")

    elif(computerMove == 0 and you == 1):
        print("You lose!")

    elif(computerMove == 0 and you == -1):
        print("You Win!")

    elif(computerMove == 1 and you == -1):
        print("You lose!")

    elif(computerMove == 1 and you == 0):
        print("You Win!")
    else:
        print("Something Went Wrong")
    


