import random
#print the program title
print("Guess a number between 1 and 100.")

#Generate a secret number by random generator 

secret = random.randint(1,100)
num_tries=0

#Ask the user to guess the number

while True:
    guess = int(input("Enter yout guess: "))
    num_tries += 1

    #compare the guess and the secret
    if guess < secret:
        print("Too Low! Guess again")
    elif guess > secret:
        print ("Too high! Guess again")
    else:
        print (f"Good! your guess is correct in {num_tries} tries")
        break
