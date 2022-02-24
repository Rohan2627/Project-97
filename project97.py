import random
number = random.randint(1,9)


chances = 5
while chances <= 5:
    guess = int(input("Guess a number from 1 to 9"))
    
    if guess == number:
        print("Congratulations you won!!")
        break

    elif guess > number:
        print("Wrong, your guess is too high, guess again")
    elif guess < number:
        print("Wrong, your guess is too low, guess again")
   
   
    chances = chances-1

if not chances < 5:
    print("You lose!! The number is", number)
     
         