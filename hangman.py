import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

current_hangman_pic_index = 0
print(HANGMANPICS[current_hangman_pic_index])

words_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
chosen_word = random.choice(words_list)
num_of_letters = ['_' for dash in range(len(chosen_word))]
num_lives = 6
print(' '.join(num_of_letters))

while num_lives > 0:
  
  user_letter_guess = input("Guess a letter: ")
  same_letter_indices = []
  if user_letter_guess in chosen_word:
    if user_letter_guess in num_of_letters:
      print(f'You already chose {user_letter_guess}.')
    if chosen_word.count(user_letter_guess) > 1:
      for i in range(len(chosen_word)):
        if chosen_word[i] == user_letter_guess:
          same_letter_indices.append(i)
      for i in same_letter_indices:
        num_of_letters[i] = user_letter_guess
    else:
      index_of_letter = chosen_word.index(user_letter_guess)
      num_of_letters[index_of_letter] = user_letter_guess
    print(' '.join(num_of_letters))
    if ''.join(num_of_letters) == chosen_word:
      print('You win!')
      break
  else:
    print(' '.join(num_of_letters))
    print(f'You guessed {user_letter_guess}, that\'s not in the word. You lose a life.')
    num_lives -= 1
    current_hangman_pic_index += 1
    print(HANGMANPICS[current_hangman_pic_index])
    if num_lives == 0:
      print(f'You lose! The word was {chosen_word}.')
