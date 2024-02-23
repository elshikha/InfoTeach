import re

from PIL import Image

def x_c(input_data, ek):
    """
    Apply XOR cipher to input data using the provided encryption key.
    """
    return bytearray(a ^ ek for a in input_data)

def e_i(input_path, ek):
    """
    Encrypt an image using XOR cipher with the given encryption key.
    Save the encrypted image to a file named 'encrypted_image.png'.
    """
    o_i = Image.open(input_path)
    o_b_d = bytearray(o_i.tobytes())
    e_d = x_c(o_b_d, ek)
    e_i = Image.frombytes(o_i.mode, o_i.size, bytes(e_d))
    e_i.save('encrypted_image.png')

def d_i(input_path, dk):
    """
    Decrypt an image using XOR cipher with the given decryption key.
    Save the decrypted image to a file named 'decrypted_image.jpg'.
    """
    e_i = Image.open(input_path)
    e_b_d = bytearray(e_i.tobytes())
    d_d = x_c(e_b_d, dk)
    d_i = Image.frombytes(e_i.mode, e_i.size, bytes(d_d))
    d_i.save('decrypted_image.jpg')

# Get user input for the operation, file path, and secret key
s_o = input("Do you want to encrypt or decrypt the image? Enter 'e' or 'd': ")
i_f_p = input("Enter the file path of the image: ")
s_k = int(input("Enter the secret key (an integer from 0 to 255): "))

# Perform the selected operation (encrypt or decrypt) on the image
if s_o.lower() == 'e':
    e_i(i_f_p, s_k)
    print("Image encrypted successfully!")
elif s_o.lower() == 'd':
    d_i(i_f_p, s_k)
    print("Image decrypted successfully!")
else:
    print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
