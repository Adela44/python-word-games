import sys
import random
from collections import defaultdict

def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            words = [line.strip() for line in f]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)


#we can use the sorted word as a key, to group the anagrams together
def generate_anagram_groups(words):
    groups = defaultdict(list) #list()  →  []

    for word in words:
        key = ''.join(sorted(word))  #eg. sorted("listen") -> ['e', 'i', 'l', 'n', 's', 't']
        groups[key].append(word)

    # Keep only groups with more than one anagram
    filtered = {}
    for key, word_list in groups.items():
        if len(word_list) > 1:
            filtered[key] = word_list

    return filtered

def anagram_finder(anagrams):
    secret_key = random.choice(list(anagrams.keys()))
    print("Welcome to anagram finder! Given a 5-letter word, try to guess one of its valid anagrams \n You only have 3 chances")
    word1 = random.choice(anagrams[secret_key])
    print(word1)
    attempts = 1
    max_attempts = 3
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        if guess in anagrams[secret_key] and guess != word1:
            print("Congratulations, you guessed the anagram!")
        attempts = attempts + 1
    if attempts > max_attempts:
        print("Too many attempts, here's the list of anagrams:")
        print(anagrams[secret_key])
    return

words = load_dictionary("5-letter-words.txt")
anagrams = generate_anagram_groups(words)
anagram_finder(anagrams)
