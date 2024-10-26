def caesar_cipher_decrypt(message: str, key: int) -> str:
    decrypted_message = []
    
    # Normalize the key to handle large numbers and negative shifts
    key = key % 26

    for char in message:
        if char.isalpha():  # Check if it's a letter
            # Determine if the letter is uppercase or lowercase
            shift = 65 if char.isupper() else 97
            
            # Shift the character within the alphabet range
            new_char = chr(((ord(char) - shift - key) % 26) + shift)
            decrypted_message.append(new_char)
        else:
            # Non-alphabetical characters are unchanged
            decrypted_message.append(char)

    return ''.join(decrypted_message)

# Enter key: 1
# Enter message: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.
# Result: The quick brown fox jumps over the lazy dog.

message = input('Enter message: ')
key = int(input('Enter key: '))

decrypted_message = caesar_cipher_decrypt(message, key)
print(decrypted_message)