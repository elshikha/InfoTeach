def caesar_cipher(data, shift, way):
    """
    Apply Caesar Cipher to the input data.

    Parameters:
    - data (str): The input text to be encrypted or decrypted.
    - shift (int): The number of positions to shift the letters in the alphabet.
    - way (str): 'e' for encryption, 'd' for decryption.

    Returns:
    - str: The result after applying Caesar Cipher to the input data.
    """

    result = ""

    for char in data:
        # Check if the character is an alphabetical letter
        if char.isalpha():
            # Determine the ASCII offset based on the case (lower or upper)
            ascii_offset = ord('a') if char.islower() else ord('A')

            # Calculate the new character after shifting
            cipher_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

            # Append the encrypted or decrypted character based on the specified way
            result += cipher_char if way == 'e' else chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            # If the character is not an alphabetical letter, keep it unchanged
            result += char

    return result


# Get user input for the text, encryption/decryption, and shift value
data = input("Please enter the text: ")
way = input("Encrypt or decrypt the text? (e/d): ")
shift = int(input("Please enter the shift value: "))

# Print the result after encryption or decryption
print(f"Text after {way}ion: {caesar_cipher(data, shift, way)}")
