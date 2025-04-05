n = 18
num_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while(num_of_guesses<=9):
    guess_num = int(input("Guess the no.: \n"))
    if guess_num<18:
        print("You enter lesser no., please input the greater no.\n")
    elif guess_num>18:
        print("You enter greater no., please input the lesser no.\n")
    else:
        print("You entered correct no.\n")
        print(num_of_guesses,"no. of guesses you took to finish.")
        break
    print(9-num_of_guesses,"no. of guesses left")
    num_of_guesses = num_of_guesses + 1

    if(num_of_guesses>9):
        print("Game Over")