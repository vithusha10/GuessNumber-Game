import random
#create a number guessing game function
def guess_number():
    attempt =0
    number = random.randint(1,100)
    max_attempt = 3

    print "Welcome to play guess number game!"
    #This can only use for latest version of python
    #print(f"Try to guess the number between 1 and 100 in {max_attempt} attempts.")

    print("Try to guess the number between 1 and 100 in {} attempts.".format(max_attempt))

    #Run a loop for attempts:
    while attempt < max_attempt:
        guess = int(input("Enter gussed no:"))

        if guess < number :
            print("Number is Too low. Try again!")
        elif guess > number :
            print("Number is Too large. Try again!")
        else:
            print("Congratulations! You guessed the number correctly!".format(number) )

            break
        attempt+1

        if attempt == max_attempt :
            print("Sorry, you've reached the maximum attempts. The number was".format(number))

if __name__ == "__main__":
    guess_number()
