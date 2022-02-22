alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
import art

def caesar(message, shift_nr, cypher_direction):
    if cypher_direction == 'encode':
        shift_nr = abs(shift_nr)
        action='encoded'
    elif cypher_direction == 'decode':
        shift_nr = -1 * abs(shift_nr)
        action = 'decoded'

    message = message.lower()
    encoded_text = ''
    for index in range(len(message)):
        letter = message[index]
        if letter in alphabet:
            index_in_alphabet = alphabet.index(letter)
            position = (index_in_alphabet + shift_nr) % len(alphabet);
            if position < 0:
                position = len(alphabet) + position
            letter = alphabet[position]
        encoded_text += letter
    print(f"The {action} text is: {encoded_text}")


print(art.logo)
exitApp = False
while not exitApp:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    continue_app = input("Continue? yes or no:\n")

    if continue_app == 'no':
        exitApp = True


