import random

#snake water gun game 
def gameWin(comp,you):
    # If two values are equal declare tie
    if comp == you:
        return None

    #Check all the possibilities if computer choose snake
    elif comp == 's':
        if you =='w':
            return False
        
        elif you =='g':
            return True

    #Check all the possibilities if computer choose water
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    #Check all the possibilities if computer choose gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you =='w':
            return True

randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

b = 'y'

while(b == "y"):
    you = input("Your Turn : Snake(s) Water(w) or Gun(G)?")
    a = gameWin(comp,you)

    print(f"Computer Choose {comp}")
    print(f"You Choose {you}")

    if a == None:
        print("Gam is Tie")

    elif a:
        print("You Win")

    else:
        print("You Lose!")

    b = input("Do You want to play more\n if yes press y \n if no press any other key")