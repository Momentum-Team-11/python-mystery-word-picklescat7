import string
mystery_word = "spoon"
mystery_word_length = (len(mystery_word))
#print(random_word_length)
player_word = ""
#hangman = ('_' * mystery_word_length)
hangman = " "
#hangman1 = " "
letter_in = " "
guess_count = 1
alphabet = [string.ascii_lowercase]
alphabet_used = []
ask_guess = " "
letter = " "

#print(type(alphabet)) it's a string

#print(f"Welcome to The Mystery Word Game! The mystery word is {mystery_word_length} letters long.")

#for i in mystery_word:  

print(f"Welcome to The Mystery Word Game! The mystery word is {mystery_word_length} letters long.")
print("................")
print("Rules: ")
print("1. You are allowed 8 guesses.")
print("2. You lose a guess only when the letter is not in the mystery")
print("3. The game ends when you have the full word or run out of guesses")
print("................")
print("")
print("")

def play_game():
  #letter = str.lower(input("Guess a letter: "))
  global player_word
  global guess_count
  global alphabet_used
  global letter
  #global hangman
  
  #hangman = " "
  #print(hangman)
  if hangman != mystery_word and guess_count < 9:
    #word_guess_display() 
    #print(hangman)
    letter1 = str.lower(input(f">>>You are on try {guess_count} of 8 -- Guess a letter: "))
    if len(letter1) != 1:
      print("Your guess must be exactly one letter from the English alphabet. Try again")
      play_game()
    if letter1 not in alphabet_used:
      letter = letter1
      guess_count += 1
      alphabet_used += letter
      letter_match()
    else:
      print("You already tried that letter. Try again")
      play_game()
  elif hangman == mystery_word and guess_count < 9:
      print(f"****WOOHOO!! You guessed the mystery word! It took you {guess_count} tries!****") 
  else: 
    print("Out of tries!!! Game over.")  
    #letter_match()
    
      #letter_in.lowercase = input("Guess a letter")
def letter_match():
  global player_word
  if letter in mystery_word:
    player_word += letter
    print("")
    print(f"Yay '{letter}' IS in the mystery word!")
    word_guess_display() 
    #print(player_word)         
  elif letter not in mystery_word: 
    print("")
    print(f"Sorry '{letter}'' is NOT in the mystery word!")
    word_guess_display() 
  
  
def word_guess_display():
  #print("letter ", letter)
  global hangman
  # global hangman1
  hangman = ""
  # #print("hangman: ", hangman)
  # # global hangman1
  # #hangman = " "
  # #while int(len(hangman)) < mystery_word_length:
  # # while hangman != mystery_word:
  for i in mystery_word: #moops
    if i in alphabet_used: #m yes
      hangman += i #hangman = m
      #print(hangman)
    # elif i in alphabet_used:
    #   hangman = hangman
    #   print(hangman)
    else:
      hangman += "_"  
      #print(hangman)
  #hangman = hangman1
  print("You've guessed: ", hangman)
  youve_guessed()
  
# y1. check if the guessed letter is in mystery_word
# 2. figure out which spot it is in and return a number ??Store as new variable??
# 3. find the correspdong number spot in hangman
# 4. replace the characcter at that corresponding number spot with the guessed letter

def youve_guessed():
  print("...")
  print(f"Letters you've guessed: {alphabet_used}")
  print("...")
  play_game()
# while guess != random_word and count < 9:
#   for letter in guess if number > random_number:
#     print("Too high! Try again.")
#     count += 1
#     number = int(input("Guess the number btw 1 and 20"))
#   if number < random_number:
#     print("too low!")
#     count += 1
#     number = int(input("Guess the number btw 1 and 20"))

  
  #if letter in mystery_word:
    #print("Yay that letter IS in the mystery!")
  #play_game()
  # if x != i:
  #     print("Sorry that letter is NOT in the mystery word!")
  #   play_game()
      #guessed_word += letter_in
  #     print(letter)
  #     for letter in mystery_word:
  #       if letter_in == letter: 
  #         guessed_word += letter_in
  #         print(guessed_word)
  # if guessed_word == mystery_word:
  #   print(f"You guessed it right! It took you {guess_count} tries!") 
  # if guessed_word != mystery_word:
  #   print("Nope that was wrong")
  #   play_game()


# if guess_count > 3:
#   print("Too many guesses. GAME OVER")

# if guessed_word == mystery_word:
#        print(f"You guessed it right! It took you {guess_count} tries!") 
  #else: 
    #play_game()
if __name__ == "__main__":
    play_game()
