import random




def word_selection():
    mylist = ["apple", "banana", "cherry"]
    mystery_word = random.choice(mylist) 
    return mystery_word

def choose_letter():
    guess = ''
    is_valid = False
    alphabet = 'abcdefghjiklmnopqrstuvwxyz'
    while not is_valid:
        guess = input("Guess a letter? ")
        if guess in alphabet and len(guess) == 1:
            is_valid = True
    return guess

def print_anything_in_list(list):
    empty=''
    for char in list:
        empty = empty+char
    print(empty)
    return empty

def print_lines(mystery_word):
    global word
    word = ["_" for i in range(len(mystery_word))]
    print_anything_in_list(word)

def print_letters_lines(mystery_word, guess):
    global word
    for i in range(len(mystery_word)):
        if guess == mystery_word[i]:
            word[i] = guess
        print_anything_in_list(word)
        
def check_letter_to_word(mystery_word, guess):
    global lives
    if guess in mystery_word:
        correct_list.append(guess)
        print_anything_in_list(correct_list)
        print("You got that letter correct")
        pass
    else:
        incorrect_list.append(guess)
        print_anything_in_list(incorrect_list)
        print("Sorry that was incorrect, you lose a life")
        lives -= 1
        pass
    


incorrect_list = []
correct_list = []
lives = 6
mystery_word = word_selection()
word = []
print_lines(mystery_word)
print(mystery_word)
while lives > 0:
    guess = choose_letter()
    check_letter_to_word(mystery_word, guess)
    print_letters_lines(mystery_word, guess)

if lives == 0:
    print("You ran out of lives")