import string

def caesar_cipher():
  ascii_characters = list(string.ascii_lowercase)
  while True:
    encode_or_decode = input("Type 'encode' to encrypt. Type 'decode' to decrypt:\n").lower()
    user_message = input("Type your message:\n").lower()
    user_message_list = list(user_message)
    shift_number = int(input("Type the shift number:\n"))
    if encode_or_decode == 'encode':
      for i in range(len(user_message)):
        index_of_current_letter_in_message = ascii_characters.index(user_message_list[i])
        if index_of_current_letter_in_message + shift_number > len(ascii_characters) - 1:
          user_message_list[i] = ascii_characters[index_of_current_letter_in_message + shift_number - len(ascii_characters)]
        else:
          user_message_list[i] = ascii_characters[index_of_current_letter_in_message + shift_number]
      print(''.join(user_message_list))
    else:
      for i in range(len(user_message)):
        index_of_current_letter_in_message = ascii_characters.index(user_message_list[i])
        if index_of_current_letter_in_message - shift_number < 0:
          user_message_list[i] = ascii_characters[len(ascii_characters) + (index_of_current_letter_in_message - shift_number)]
        else:
          user_message_list[i] = ascii_characters[index_of_current_letter_in_message - shift_number]
      print(''.join(user_message_list))
    retry = input("Would you like to go again? Type 'yes' to continue. Otherwise type 'no'\n").lower()
    if retry == 'yes':
      continue
    else:
      break

caesar_cipher()
