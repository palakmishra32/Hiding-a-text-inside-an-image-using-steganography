# Steganography
**Project Title: Hiding a Text Inside an Image Using Steganography**

Description:

This project demonstrates an implementation of RGB steganography, which hides a secret message within the pixel values of an image. Using an XOR operation with a provided security key, the ASCII values of the text are embedded into the RGB channels of the image. The project includes both encoding and decoding functionalities, allowing users to securely hide and retrieve sensitive information within images.

Features:

1. Text Encoding: Converts the secret message into ASCII values and embeds them into the RGB channels of the image using XOR 
   operation.
2. Text Decoding: Retrieves the hidden message by reversing the XOR operation using the same security key.
3. Security: Uses a user-provided key to ensure that the hidden message can only be decoded by someone with the correct key.
4. Simple Interface: Easy-to-use input prompts for entering the key and the message to be hidden.
