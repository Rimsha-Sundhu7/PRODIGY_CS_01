def encrypt_decrypt(text, mode, key):
    # Define the letters and number of letters in the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'
    num_letters = len(letters)

    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if letter in letters:
            index = letters.find(letter)
            new_index = (index + key) % num_letters
            result += letters[new_index]
        else:
            result += letter  # Include spaces and other characters unchanged

    return result


print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
else:
    print('Invalid mode selected. Please choose "e" for encryption or "d" for decryption.')
