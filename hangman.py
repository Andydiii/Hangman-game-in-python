import random
import string
from words import words_list

def get_valid_word(words_list):
    target_word = random.choice(words_list)
    while '-' in target_word or ' ' in target_word:
        target_word = random.choice(words_list)
    return target_word

def hangman():
    lives = 6
    word = get_valid_word(words_list)
    word_letters = set(word) #letters in the target word
    all_possible_letter = set(string.ascii_lowercase)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        #letter that already used
        print('you have', lives, 'lives left and you have already used these words:', ' '.join(used_letters))

        #current words_list
        curr_word_list = [letter if letter in used_letters else '_' for letter in word]
        print("current_word:", ' '.join(curr_word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in all_possible_letter - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("letter is not in the word")
        
        elif user_letter in used_letters:
            print("pls guess other letters that you havent guessed")
         
        else:
            print("please enter a valid character")
        print("\n")
    if lives == 0:
        print('sorry, you died. The word is', word)
    else:
        print("congrats!!! you got it! The word is", word)

hangman()



