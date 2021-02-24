# Calculator Program

def add_nums(num_one, num_two):
  return num_one + num_two
def subtract_nums(num_one, num_two):
  return num_one - num_two
def multiply_nums(num_one, num_two):
  return num_one * num_two
def divide_nums(num_one, num_two):
  return num_one / num_two
while True:
  number_one = int(input("What's the first number? "))
  print('+\n-\n*\n/')
  pick_operation = input("Pick an operation: ")
  number_two = int(input("What's the second number? "))

  operations = {'+': add_nums(number_one, number_two), '-': subtract_nums(number_one, number_two), '*': multiply_nums(number_one, number_two), '/': divide_nums(number_one, number_two)}

  if pick_operation in operations.keys():
    print(f"{number_one} {pick_operation} {number_two} = {operations[pick_operation]}")
  repeat_again = input("Would you like to perform another calculation? Type 'y' or 'n': ").lower()
  if repeat_again == 'y':
    continue
  else:
    break
