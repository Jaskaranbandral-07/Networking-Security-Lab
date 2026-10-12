# Caesar Cipher

text = input("Enter plaintext: ")
shift = int(input("Enter shift: "))

encrypted = ""

# Encryption
for char in text:
    if char.isalpha():
        encrypted += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
    else:
        encrypted += char

decrypted = ""

# Decryption
for char in encrypted:
    if char.isalpha():
        decrypted += chr((ord(char.upper()) - 65 - shift) % 26 + 65)
    else:
        decrypted += char

print("\nCAESAR CIPHER")
print("Plaintext :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
print("Verification:", decrypted == text.upper())
