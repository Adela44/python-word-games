import random
import sys

#each line contains one word and its definition in the form of : word - definition
def load_dictionary(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            word_defs = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                word, definition = line.split(" - ", 1) # Split only on the first " - "
                word_defs[word] = definition
            return word_defs

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

def shuffle_word(word):
    char_list = list(word)
    random.shuffle(char_list)
    return ''.join(char_list)

def unscramble(words):
    print("This is Word Scramble! You have 3 chances to guess the correct word")
    secret_word = random.choice(list(words.keys()))

    print("The shuffled word is: ", shuffle_word(secret_word))
    print("Original word definition: ", words[secret_word])
    attempts = 1
    max_attempts = 3
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        if guess == secret_word:
            print("Congratulations, you guessed it!")
            break
        attempts = attempts + 1
    if attempts > max_attempts:
        print("Too many attempts, the correct word was:", secret_word)
        print(secret_word)

words = load_dictionary("common_words_145.txt")
unscramble(words)