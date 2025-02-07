def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_offset = ord('A')
            else:
                shift_offset = ord('a')
            shifted = (ord(char) - shift_offset + (shift * mode)) % 26 + shift_offset
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1)

def decrypt(text, shift):
    return caesar_cipher(text, shift, -1)

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")

    if choice.lower() == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
