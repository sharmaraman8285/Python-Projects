# Rock(r), Paper(p), Scissor(s) Game in Python :-----

''' 
Created By : Raman Sharma
Game Name : Rock(r), Paper(p), Scissor(s)
Language Used : Python(3.6)
'''
#import random for calling random numers:
import random

#created function as game :
def game(comp,you):
#exit if user enter wrong input other than (r),(s),(p): 
    # if you!= 'p' and 's' and 'r':
    #     print("Please Enter Valid Value")
    #     exit("Try agian with valid Input ")
# Putting Condition if user enters b/w (r),(p),(s):
    if comp == you:
        return None
    elif comp == 'p':
        if you == 's':
            return True
        elif you =='r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
print("Computer already select's from :Scissor(s) , Paper(p) , Rock(r)")
print("NOW YOUR's TURN ")
#initialize random for getting random value b/w 1 to 3:
randNo=random.randint(1,3)
#values change to string:
if randNo ==1:
    comp = 's'
elif randNo ==2:
    comp = 'p'
elif randNo == 3:
    comp = 'r'

you =input("Select One from this :\n Scissor(s) , Paper(p) , Rock(r) : "  )
a = game(comp ,you)
print(f"Computer Chooses : {comp}")
print(f"You Chooses : {you}")

#output of Results:
if a == None:
    print("This game is tied, Try Again to Win ")
elif a:
    print("You Win")
else:
    print("you loose")