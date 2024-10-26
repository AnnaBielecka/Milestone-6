def caesar_cipher_encrypt(message: str, key: int) -> str:
    encrypted_message = []
    
    # Normalize the key to handle large numbers and negative shifts
    key = key % 26

    for char in message:
        if char.isalpha():  # Check if it's a letter
            # Determine if the letter is uppercase or lowercase
            shift = 65 if char.isupper() else 97
            
            # Shift the character within the alphabet range
            new_char = chr(((ord(char) - shift + key) % 26) + shift)
            encrypted_message.append(new_char)
        else:
            # Non-alphabetical characters are unchanged
            encrypted_message.append(char)

    return ''.join(encrypted_message)

# Enter key: 1
# Enter message: The quick brown fox jumps over the lazy dog.
# Result: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.   

message = input('Enter message: ')
key = int(input('Enter key: '))

encrypted_message = caesar_cipher_encrypt(message, key)
print(encrypted_message)