import random

random_number = random.randrange(1, 20)

guesses = 0
num_of_attempts = 10

while True:
    guess_num = input("\nGuess the number: ")
    if guess_num.isdigit():
        guess_num = int(guess_num)
        if guess_num == random_number:
            guesses +=1
            print("\nNumber of guesses: ", guesses, "\nCongratulations! you guess the correct number: ", random_number)
            print("\nYou got right guess in ", guesses,"attempt(s)\n")
            break
   
        elif guess_num < random_number:
            guesses +=1
            print("\nNumber of guesses: ", guesses,"\nNumber should be greater")
            num_of_attempts -= 1
            print("Remaining number of attempts are: ", num_of_attempts, "\n")
        else:
            guesses +=1
            print("\nNumber of guesses: ", guesses,"\nNumber should be lesser")
            num_of_attempts -= 1
            print("Remaining number of attempts are: ", num_of_attempts,"\n")

    else:
        print("Please enter number next time\n")
        break
    
    if num_of_attempts == 0:
        print("\nAttempts are finished!\n")
        break
