import re

def cc(data, shift, way):
    r = ""

    for c in data:
        # Check if the character is an alphabetical letter
        if c.isalpha():
            # Determine the ASCII offset based on the case (lower or upper)
            o = ord('a') if c.islower() else ord('A')

            # Calculate the new character after shifting
            cipher_char = chr((ord(c) - o + shift) % 26 + o)

            # Append the encrypted or decrypted character based on the specified way
            r += cipher_char if way == 'e' else chr((ord(c) - o - shift) % 26 + o)
        else:
            # If the character is not an alphabetical letter, keep it unchanged
            r += c

    return r


# Get user input for the text, encryption/decryption, and shift value
d = input("Please enter the text: ")
w = input("Encrypt or decrypt the text? (e/d): ")
s = int(input("Please enter the shift value: "))

# Print the result after encryption or decryption
print(f"Text after {w}ion: {cc(d, s, w)}")
