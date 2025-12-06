import sys
import random

def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            words = []
            for line in f:
                words.append(line.strip())
            return words
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

def is_valid_guess(guess, guesses):
    return guess in guesses # check if the word exists in the guesses list

def missing_letters(guesses):
    print("Welcome to Missing Letters! You have 5 chances to guess the 6-letter-word secret word that fits")
    list1 = [0,1,2,3,4,5]
    target_word = random.choice(guesses)
    temp_list = list(target_word)
    missing_letter1 = random.choice(list1)
    list1.remove(missing_letter1)
    missing_letter2 = random.choice(list1) # to avoid random picking the same letter
    temp_list[missing_letter1] = "_"
    temp_list[missing_letter2] = "_"
    display_word = "".join(temp_list)
    print("Here's your word: ", display_word)
    attempts = 1
    max_attempts = 5
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower() #makes the letter lowercase
        if guess not in guesses:
            print("Invalid guess. Please enter a valid 6-letter-word or a more common one")
        if guess == target_word: # the correct guess
            print("You guessed the word! Congratulations! ",target_word)
            break
        attempts += 1 #else continue with the attempts
        if attempts > max_attempts:
            print("Too many attempts. The secret word was: " + target_word)

guesses = load_dictionary("6-letter-words.txt")
missing_letters(guesses)
