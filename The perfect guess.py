#we are going to write a program that generates a random number and asks the user to guess it.

import random

randNo=random.randint(1,100)

userGuess=None
guesses=0

while(userGuess!=randNo):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if userGuess==randNo:
        print("You guessed it right!")
       
    else:
        
        if(userGuess>randNo):
            print("wrong!Lower your guessing range!")
            
        else:
            print("wrong!Enhance your guessing range")
           
        

print(f"You guessed right in {guesses} steps")

with open('hiscore.txt')  as f:
    data=int(f.read())


if data=='':
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))
elif (data)>(guesses):
    print("You have broken the highscore!")
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))