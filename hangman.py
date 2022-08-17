import random
from re import A
import string
from words import words_list


def get_valid_word(words_list):
    target_word = random.choice(words_list)
    while '-' in target_word or ' ' in target_word:
        target_word = random.choice(words_list)
    return target_word

def hangman():
    word = get_valid_word(words_list)
    word_letters = set(word) #letters in the target word
    all_possible_letter = set(string.ascii_lowercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("you have already used these words:", ' '.join(used_letters))

        #current words_list
        curr_word_list = [letter if letter in used_letters else '_' for letter in word]
        print("current_word:", ' '.join(curr_word_list))
        #print("\n")


        user_letter = input("Guess a letter: ").lower()
        if user_letter in all_possible_letter - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("pls guess other letters that you havent guessed")
         
        else:
            print("please enter a valid character")
        print("\n")
        
    print("congrats!!! you got it!", f"The word is {word}")
hangman()



