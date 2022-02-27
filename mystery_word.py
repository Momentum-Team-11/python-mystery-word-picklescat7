import string #need this for line 11
import sys #need for exit
mystery_word = " "
mystery_word_length = (len(mystery_word))
word_easy = []
word_medium = []
word_hard = []
#print(random_word_length)
#player_word = ""
#hangman = ('_' * mystery_word_length)
hangman = " "
letter_in = " "
guess_count = 1
guess_count1 = 0
alphabet = [string.ascii_lowercase]
alphabet_used = []
play_again = " "
letter = " "
level = 0

def intro_text():
    print("Welcome to The Mystery Word Game!")
    print("................")
    print("Rules: ")
    print("1. You are allowed 8 guesses.")
    print("2. You lose a guess only when the letter is not in the mystery")
    print("3. The game ends when you have the full word or run out of guesses")
    print("................")

def how_hard():
    global level
    print("How hard you like the game to be?") 
    print("")
    print("1 - Easy | 4-6 letter words")
    print("2 - Medium | 6-8 letter words")
    print("3 - Easy | 8+ letter words")
    print("")
    level = (int(input("Select a difficulty (1, 2 or 3): ")))
    print(f"You selected level: {level}")
    print(type(level))

def play_game():
    global guess_count 
    global alphabet_used
    global alphabet
    global letter
    global mystery_word
    global guess_count1 
    global level 
    global word_easy
    global word_medium
    global word_hard
    print(" ")
    if guess_count1 == 0: #aka first turn only
        intro_text()
        how_hard()
        guess_count1 += 1
        import random
        with open("words.txt", "r") as file:
            all_text = file.read()
        word = list(map(str, all_text.split()))
        if level == 1:
            for x in word: 
                if len(x) <= 6:
                    word_easy.append(x)
        #if level == 1:
            mystery_word = (random.choice(word_easy)) 
        if level == 2:
            for x in word: 
                if len(x) >= 6 and len(x)<=8:
                    word_medium.append(x)
            mystery_word = (random.choice(word_medium))
        if level == 3:
            for x in word: 
                if len(x) >= 8:
                    word_hard.append(x)
            mystery_word = (random.choice(word_hard))        
        #word_easy = [x for x in word if len(word) < 6]
        
        mystery_word_length = (len(mystery_word))
        print(mystery_word)
        file.close()
        print(" ")
        print(f"@@@The mystery word is {mystery_word_length} letters long.@@@")
        print(" ")
        play_game()
    else: 
        while guess_count1 != 0:
            if hangman != mystery_word and guess_count < 9:
                letter1 = str.lower(input(f">>>You are on try {guess_count} of 8 -- Guess a letter: "))
                if letter1.isdigit():
                    print("!!!")
                    print("Your guess must be exactly one letter from the English alphabet. Try again")
                    print(" ")
                    #play_game()
                if len(letter1) != 1:
                    print("!!!")
                    print("Your guess must be exactly one letter from the English alphabet. Try again")
                    print(" ")
                    #play_game()
                if letter1 not in alphabet_used:
                    guess_count1 += 1
                    letter = letter1
                    alphabet_used += letter #I already forget why I was using letter1 and letter
                    letter_match()
                else:
                    print("!!!")
                    print("You already tried that letter. Try again")
                    
            elif hangman == mystery_word and guess_count < 9:
                print(f"****WOOHOO!! You guessed the mystery word!!****") 
                play_again() 
            else: 
                print("Out of tries!!! Game over.")  
                print(f"The mystery word was {mystery_word}")
                play_again()
    
def letter_match():
    global mystery_word
    global guess_count
    if letter in mystery_word:
        while hangman != mystery_word:
            print(" ")
            print(f"Yay '{letter}' IS in the mystery word!")
            print(" ")
            word_guess_display()
    elif letter not in mystery_word:
        guess_count += 1 
        print(" ")
        print(f"Sorry '{letter}'' is NOT in the mystery word!")
        print(" ")
        word_guess_display()

def word_guess_display():    
    global hangman
    hangman = ""
    for i in mystery_word: 
        if i in alphabet_used: 
            hangman += i 
        else:
            hangman += "_"  
    print("  Player word guess:", hangman)
    print(" ")
    youve_guessed()


def youve_guessed():
    if hangman != mystery_word:
        print("........................................")
        print(f"Letters you've guessed: {alphabet_used}")
        print("........................................")
        #print(" ")
        play_game()
    else:
        play_game()

def play_again():
    global guess_count 
    global guess_count1
    global alphabet_used
    global hangman
    print(" ")
    print("...................................")
    ask_again = (input("Do you want to play again? y/n"))
    if ask_again == 'y':
        guess_count = 1
        guess_count1 = 0
        alphabet_used = []
        hangman = ""
        print(" ")
        print(" ")
        play_game()
    if ask_again == 'n':
        print("Oh that's too bad. See you later!")
        sys.exit()

if __name__ == "__main__":
    play_game()
