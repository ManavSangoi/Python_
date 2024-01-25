def game():
    if comp==Player:
        print("Computer has selected "+comp)
        print("Player has selected "+Player)
        print("Its a tie")
    elif comp=='st':
        if Player=='p':
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Player wins")
        else:
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Computer wins")
    elif comp=='p':
        if Player=='sc':
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Player wins")
        else:
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Computer wins")
    elif comp=='sc':
        if Player=='st':
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Player wins")
        else:
         print("Computer has selected "+comp)
         print("Player has selected "+Player)
         print("Computer wins")          
from ast import Break
from random import randint
i=randint(1,3)
#print (i)
if i==1:
    comp='st'
elif i==2:
    comp='p'
elif i==3:
    comp='sc'
    
Player=input("Enter st for Stone,p for Paper,sc for Scissors:")
if Player=='st' or Player=='p' or Player=='sc':
    game()
else:
    print("Enter a valid input")