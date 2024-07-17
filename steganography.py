import cv2
import os

# Create dictionaries for encoding and decoding characters
char_to_int = {chr(i): i for i in range(256)}
int_to_char = {i: chr(i) for i in range(256)}

# Reading the image
image_path = r"C:\Users\Sneha\OneDrive\Desktop\stegano\flower.jpg"
image = cv2.imread(image_path)

rows, cols, _ = image.shape
print("Image dimensions:", rows, cols)

# Getting user inputs for key and text to hide
key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

# Encoding the text in the image
key_index = 0
text_index = 0
text_length = len(text)

for row in range(rows):
    for col in range(cols):
        for channel in range(3):  # Iterate over R, G, B channels
            if text_index < text_length:
                char_value = char_to_int[text[text_index]]
                key_value = char_to_int[key[key_index % len(key)]]
                image[row, col, channel] = char_value ^ key_value

                text_index += 1
                key_index += 1

encoded_image_path = "encoded_image.png"
cv2.imwrite(encoded_image_path, image)
print("Data hiding in image completed successfully.")
os.startfile(encoded_image_path)

# Decoding the text from the image
encoded_image = cv2.imread(encoded_image_path)
decoded_text = ""
key_index = 0
text_index = 0

key_for_decoding = input("Enter key to decode the message: ")

if key != key_for_decoding:
    print("Incorrect key! Unable to decode the message.")
else:
    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # Iterate over R, G, B channels
                if text_index < text_length:
                    encoded_value = encoded_image[row, col, channel]
                    key_value = char_to_int[key[key_index % len(key)]]
                    decoded_char = int_to_char[encoded_value ^ key_value]
                    decoded_text += decoded_char

                    text_index += 1
                    key_index += 1

    print("Decoded text:", decoded_text)
