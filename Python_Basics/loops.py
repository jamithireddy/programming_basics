# While loops:
# use ctrl + c to break an infinite loop
from random import randint
print("Lets play a guessing game!")
start = input("Do you want to play?(Y/N): ")

if start.lower() == 'y':
    print("I have guessed an integer  between 0 and 25. You guess the number")
    num = randint(0, 26)
    n = 1
    while True:
        guess = int(input("Guess the  number: "))
        if guess == num:
            print("Bingo! you got it in {0} Guesses!".format(n))
            exit()
        elif abs(guess-num) > 5:
            print(
                "You have used {0} guesses and Yet you are too far away...".format(n))
        else:
            print("You have used {0} guesses to be so close....".format(n))
        n += 1
else:
    print(" Okay! Have a great day!")
