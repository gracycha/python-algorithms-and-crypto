# Vigenère Cipher Implementation in Python

select = input('Type "e" to encrypt, or "d" to decrypt: ').lower()

if select not in ['e', 'd']:
    print('Invalid option. Please type "e" or "d".')
    exit()
elif select == 'e':
    text = input('Enter the text to encrypt: ')
elif select == 'd':
    text = input('Enter the text to decrypt: ')

custom_key = input('Enter the key: ')


if select == 'e':
    direction = 1
elif select == 'd':
    direction = -1
else:
    print('Invalid option. Please type "e" or "d".')
    exit()

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
decryption = decrypt(text, custom_key)
  
if select == 'e':
    print(f'Encrypted text: {encryption}\n')
elif select == 'd':
    print(f'Decrypted text: {decryption}\n')


