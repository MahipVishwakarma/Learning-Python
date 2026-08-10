alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    shifted_text = ""
    for letter in original_text:
        shifted_number = alphabet.index(letter) + shift_amount
        shifted_number %= len(alphabet)
        shifted_text += alphabet[shifted_number]
    print(shifted_text)

def decrypt(original_text, shift_amount):
    shifted_text = ""
    for letter in original_text:
        shifted_number = alphabet.index(letter) - shift_amount
        shifted_number %= len(alphabet)
        shifted_text += alphabet[shifted_number]
    print(shifted_text)

finished = ""

while not finished == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":  
        decrypt(text, shift)

    finished = input("Are you done? (Y/N)").lower()

print("Goodbye.")