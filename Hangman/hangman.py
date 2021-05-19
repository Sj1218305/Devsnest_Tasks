import string
from words import choose_word
from images import IMAGES
import random 
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def give_hint(letters_guessed,secret_word):

    letters_left = secret_word
    index = 0
    while(index < len(letters_guessed)):
        if(letters_guessed[index] in letters_left):
            letters_left = letters_left.replace(letters_guessed[index],'')
        index +=1

    return random.choice(letters_left)

def is_valid(input_word):
    if(input_word == "hint"):
        return 2
    elif(len(input_word) == 1 and (ord(input_word) >= 97 and ord(input_word) <= 122)):
        return 1
    return 0        

def show_image(wrong_guess):
    return IMAGES[wrong_guess-1]
    


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    index = 0
    while(index < len(letters_guessed)):
        if(letters_guessed[index] == '_'):
            return False
        index += 1
        
    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    index = 0
    while(index < len(letters_guessed)):
        if(letters_guessed[index] in letters_left):
            letters_left = letters_left.replace(letters_guessed[index],'')
        index +=1

    return letters_left


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []    
    remaining_lives = 8
    wrong_guess = 0
    HINT = 1


    while(remaining_lives):
        available_letters = get_available_letters(letters_guessed) #abc...z
        print("Available letters: {} ".format(available_letters))
        print("Remaining lives: {} ".format(remaining_lives))
        print("Hint: {}. Type `hint` to use".format(HINT))
        
        guess = input("Please guess a letter: ")
        
        if(is_valid(guess) == 1):
            letter = guess.lower()
            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if is_word_guessed(secret_word, guessed_word) == True:
                    print(" * * Congratulations, you won! * * ", end='\n\n')
                    break
            else:
                remaining_lives -= 1
                wrong_guess += 1
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                print(show_image(wrong_guess))
                letters_guessed.append(letter)
                print("")
        elif(is_valid(guess) == 2):
            if not HINT:
                print("You can use the hint only once!!")
            else:
                HINT -=1
                hint = give_hint(letters_guessed,secret_word)
                print("Your hint: {}".format(hint),end='\n\n')
        else:
            print("Your input {} is invalid. Only small-case alphabets are allowed".format(guess),end='\n\n')

                

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
