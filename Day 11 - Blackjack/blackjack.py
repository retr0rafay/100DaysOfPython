import random

GOAL = 21
dealer_first_card = random.choice([num for num in range(2, 11)])

def user_play():
  card_numbers = [num for num in range(2, 10)]
  user_cards = [random.choice(card_numbers) for num in range(2)]
  dealer_cards = dealer_hand()
  print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
  print(f'Dealer\'s first card: {dealer_first_card}')
  while True:
    user_draw = input('Would you like to draw a card? Type \'y\' or \'n\': ').lower()
    if user_draw == 'y':
      user_cards.append(random.choice(card_numbers))
      print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
      print(f'Dealer\'s first card: {dealer_first_card}')
      if sum(user_cards) > GOAL:
        print(f'Your final hand: {user_cards}, final score: {sum(user_cards)}')
        print(f'Dealer\'s final hand: {dealer_cards}, final_score: {sum(dealer_cards)}')
        print('You went over! You lose!')
        break
    else:
      print(f'Your final hand: {user_cards}, final score: {sum(user_cards)}')
      print(f'Dealer\'s final hand: {dealer_cards}, final_score: {sum(dealer_cards)}')
      if sum(user_cards) > sum(dealer_cards):
        print('You win!')
      elif sum(user_cards) == sum(dealer_cards):
        print('It\'s a draw!')
      else:
        print('You lose!')
      break

def dealer_hand():
  card_numbers = [num for num in range(2, 10)]
  dealer_cards = [dealer_first_card]
  while sum(dealer_cards) < 17:
    dealer_cards.append(random.choice(card_numbers))
  return dealer_cards


while True:
  play_blackjack = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
  if play_blackjack == 'y':
    user_play()
  else:
    break
