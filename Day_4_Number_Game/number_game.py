import random
def guess_number():
    user_name = input("What is your name? ")
    print(f"Well {user_name}, I have thought of a number between 1 - 100 and you have 8 tries to guess it")
    ran_num = random.randint(1,100)
    counter = 0
    while counter < 8:
        counter += 1
        guess = int(input("What is your guess?"))
        if guess == ran_num:
            print("You guessed it!")
            print(f"It took you {counter} number of tries to guess it")
            break
        if guess > 100 and guess < 1:
            print("You guess is out of bounds")
        elif guess > ran_num:
            print("Your guess is higher")
        elif guess < ran_num:
            print("Your guess is lower")

    if guess != ran_num:
        print(f"Sorry you have ran out of attempts, the number was {ran_num}")

guess_number()