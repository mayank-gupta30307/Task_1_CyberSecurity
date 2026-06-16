import argparse



def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_file(filename, shift):
    with open(filename, "r", encoding="utf-8") as f:
        plaintext = f.read()
    ciphertext = caesar_encrypt(plaintext, shift)
    with open(filename + ".enc", "w", encoding="utf-8") as f:
        f.write(ciphertext)
    print("Encrypted:", filename + ".enc")

def decrypt_file(filename, shift):
    with open(filename, "r", encoding="utf-8") as f:
        ciphertext = f.read()
    plaintext = caesar_decrypt(ciphertext, shift)
    output = filename.replace(".enc", ".dec")
    with open(output, "w", encoding="utf-8") as f:
        f.write(plaintext)
    print("Decrypted:", output)


parser = argparse.ArgumentParser()
parser.add_argument("mode",choices=["encrypt", "decrypt"])
parser.add_argument("file")
parser.add_argument("--shift", type=int, required=True)
args = parser.parse_args()
if args.mode == "encrypt":
    encrypt_file(args.file, args.shift)
else:
    decrypt_file(args.file, args.shift)