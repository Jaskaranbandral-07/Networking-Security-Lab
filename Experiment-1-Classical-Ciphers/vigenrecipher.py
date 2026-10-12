# Vigenere Cipher

text = input("Enter plaintext: ")
key = input("Enter key: ").upper()

encrypted = ""

# Encryption
for i in range(len(text)):
    p = ord(text[i].upper()) - 65
    k = ord(key[i % len(key)]) - 65
    encrypted += chr((p + k) % 26 + 65)

decrypted = ""

# Decryption
for i in range(len(encrypted)):
    c = ord(encrypted[i]) - 65
    k = ord(key[i % len(key)]) - 65
    decrypted += chr((c - k) % 26 + 65)

print("\nVIGENERE CIPHER")
print("Plaintext :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
print("Verification:", decrypted == text.upper())
