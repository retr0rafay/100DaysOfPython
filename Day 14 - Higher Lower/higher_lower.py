import random
from game_data import data

# Create a variable to keep score
score = 0
celeb_list = []

# Create a function that will compare two random dicts
def compare_celebs():
  global score
  while True:
    celebrities = get_celebs()
    print(f'Compare A: {celebrities[0]["name"]}, a {celebrities[0]["description"]}, from {celebrities[0]["country"]}')
    print(f'Against B: {celebrities[1]["name"]}, a {celebrities[1]["description"]}, from {celebrities[1]["country"]}')
    pick_celeb = input('Who has more followers? Type "A" or "B": ').upper()
    if pick_celeb == 'A':
      if celebrities[0]['follower_count'] > celebrities[1]['follower_count']:
        score += 1
        print(f'That\'s right! Your score is {score}')
      else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        break
    elif pick_celeb == 'B':
      if celebrities[1]['follower_count'] > celebrities[0]['follower_count']:
        score += 1
        print(f'That\'s right! Your score is {score}')
      else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        break

# Create a function that will generate the dicts
def get_celebs():
  global score
  global celeb_list
  if score == 0:
    celeb_list = random.choices(data, k=2)
  else:
    current_celeb_list = celeb_list
    celeb_list = []
    celeb_list.append(current_celeb_list[1])
    celeb_list.append(random.choice(data))

  return celeb_list

compare_celebs()
