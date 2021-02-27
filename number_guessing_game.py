import random

num_of_attempts = 0
computer_number = random.choice([num for num in range(1, 101)])
difficulty = ''


def play_guessing_game():
  global num_of_attempts
  global difficulty
  difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
  if difficulty == 'easy':
    num_of_attempts = 10
  else:
    num_of_attempts = 5
  print(f'You have {num_of_attempts} attempts remaining to guess the number.')
  while True:
    if num_of_attempts == 0:
      print('You\'ve run out of guesses. You lose.')
      break
    user_number = int(input('Make a guess: '))
    if user_number == computer_number:
      print(f'You got it! The answer was {computer_number}!')
      break
    elif user_number > computer_number:
      print('Too high.')
      num_of_attempts -= 1
      if num_of_attempts == 0:
        print('You\'ve run out of guesses. You lose.')
        break
      print('Guess again.')
      print(f'You have {num_of_attempts} attempts remaining.')
      continue
    else:
      print('Too low.')
      num_of_attempts -= 1
      if num_of_attempts == 0:
        print('You\'ve run out of guesses. You lose.')
        break
      print('Guess again.')
      print(f'You have {num_of_attempts} attempts remaining.')
      continue
  

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
print('Pssst, the correct answer is 21 😉')
play_guessing_game()
