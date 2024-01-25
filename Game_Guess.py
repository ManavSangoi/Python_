from random import randint
i=randint(1,100)
print("Guess the number from 1 to 100")
for b in range (4):
 a=int(input("Enter the number:"))
 if a==i:
    print("Congratualations you have guessed the number")
    break
 elif a>i:
    print("Guess a smaller number")
 else:
    print("Guess a Larger  number")

print ("The number was",i)