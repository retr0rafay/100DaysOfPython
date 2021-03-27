PLACEHOLDER = '[name]'

with open('Input/Letters/starting_letter.txt') as starting_letter:
    content = starting_letter.readlines()
    with open('Input/Names/invited_names.txt') as invitees:
        names = invitees.readlines()
        for i in range(len(names)):
            names[i] = names[i].strip('\n')
            with open(f'Output/ReadyToSend/letter_for_{names[i]}.txt', 'w+') as invite:
                invite_content = content.copy()
                invite_content[0] = invite_content[0].replace(PLACEHOLDER, names[i])
                invite.writelines(invite_content)
                print(invite_content)
