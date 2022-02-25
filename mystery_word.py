def play_game():
    pass
import string
mystery_word = "dream"
mystery_word_length = (len(mystery_word))
#print(random_word_length)
guessed_word = " "
hangman = " "
letter_in = " "
guess_count = 1
alphabet = string.ascii_lowercase
alphabet_used = " "
ask_guess = " "
#print(type(alphabet)) it's a string

#print(f"Welcome to The Mystery Word Game! The mystery word is {mystery_word_length} letters long.")

print(f"Welcome to The Mystery Word Game! The mystery word is {mystery_word_length} letters long.")
def play_game():
  letter = str.lower(input("Guess a letter: "))
  print(letter)
  global guessed_word
  global guess_count
  while guessed_word != mystery_word and guess_count < 3:
    ask_guess = str.lower(input("Do you want to guess the word? y/n "))
    if ask_guess == 'y':
      guess_count += 1
      guess_word_yes()
    if ask_guess == 'n':
      letter = str.lower(input("Guess a letter: "))
      #guessed_word += letter_in
      print(letter)
      for letter in mystery_word:
        if letter_in == letter: 
          guessed_word += letter_in
          print(guessed_word)
      #letter_in.lowercase = input("Guess a letter")


# while guess != random_word and count < 9:
#   for letter in guess if number > random_number:
#     print("Too high! Try again.")
#     count += 1
#     number = int(input("Guess the number btw 1 and 20"))
#   if number < random_number:
#     print("too low!")
#     count += 1
#     number = int(input("Guess the number btw 1 and 20"))
def guess_word_yes():
  guess_word = str.lower(input("What is your guess? "))
  #global guess_count
  if guessed_word == mystery_word:
    print(f"You guessed it right! It took you {guess_count} tries!") 
  if guessed_word != mystery_word:
    print("Nope that was wrong")
    play_game()


# if guess_count > 3:
#   print("Too many guesses. GAME OVER")

# if guessed_word == mystery_word:
#        print(f"You guessed it right! It took you {guess_count} tries!") 
  #else: 
    #play_game()

if __name__ == "__main__":
    play_game()
