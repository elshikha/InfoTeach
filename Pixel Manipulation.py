from PIL import Image

def xor_cipher(input_data, encryption_key):
    """
    Apply XOR cipher to input data using the provided encryption key.
    """
    return bytearray(a ^ encryption_key for a in input_data)

def encrypt_image(input_path, encryption_key):
    """
    Encrypt an image using XOR cipher with the given encryption key.
    Save the encrypted image to a file named 'encrypted_image.png'.
    """
    original_image = Image.open(input_path)
    original_byte_data = bytearray(original_image.tobytes())
    encrypted_data = xor_cipher(original_byte_data, encryption_key)
    encrypted_image = Image.frombytes(original_image.mode, original_image.size, bytes(encrypted_data))
    encrypted_image.save('encrypted_image.png')

def decrypt_image(input_path, decryption_key):
    """
    Decrypt an image using XOR cipher with the given decryption key.
    Save the decrypted image to a file named 'decrypted_image.jpg'.
    """
    encrypted_image = Image.open(input_path)
    encrypted_byte_data = bytearray(encrypted_image.tobytes())
    decrypted_data = xor_cipher(encrypted_byte_data, decryption_key)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, bytes(decrypted_data))
    decrypted_image.save('decrypted_image.jpg')


# Get user input for the operation, file path, and secret key
selected_operation = input("Do you want to encrypt or decrypt the image? Enter 'e' or 'd': ")
image_file_path = input("Enter the file path of the image: ")
secret_key = int(input("Enter the secret key (an integer from 0 to 255): "))

# Perform the selected operation (encrypt or decrypt) on the image
if selected_operation.lower() == 'e':
    encrypt_image(image_file_path, secret_key)
    print("Image encrypted successfully!")
elif selected_operation.lower() == 'd':
    decrypt_image(image_file_path, secret_key)
    print("Image decrypted successfully!")
else:
    print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
