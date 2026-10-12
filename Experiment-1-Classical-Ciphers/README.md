# Experiment 1: Classical Substitution Ciphers (Caesar & Vigenère)

## 🎯 Aim & Objectives
To implement, analyze, and verify classical symmetric encryption algorithms in Python:
- **Monoalphabetic Shift Cipher (Caesar Cipher)**
- **Polyalphabetic Substitution Cipher (Vigenère Cipher)**

Understand modular arithmetic in cryptography, key generation, encryption and decryption cycles, and their vulnerability to statistical frequency analysis.

---

## 📚 Theoretical Background

### 1. Caesar Cipher (Monoalphabetic Substitution)
The Caesar cipher is one of the oldest known substitution ciphers, attributed to Julius Caesar for secure military communications. It shifts each plaintext letter by a fixed key value $k$ ($0 \le k < 26$) along the alphabet.

- **Encryption Formula:**
  $$C_i = (P_i + k) \pmod{26}$$
- **Decryption Formula:**
  $$P_i = (C_i - k) \pmod{26}$$

#### Security Weaknesses:
- Key space is extremely limited ($|\mathcal{K}| = 25$ non-trivial shifts).
- Vulnerable to instant brute-force attacks.
- Preserves single-letter frequency distribution of the underlying language (e.g., 'E', 'T', 'A' remain identifiable).

---

### 2. Vigenère Cipher (Polyalphabetic Substitution)
The Vigenère cipher uses a repeating keyword string $K$ of length $m$ to dynamically change the shift value for each character position, flattening unigram frequency analysis.

- **Encryption Formula:**
  $$C_i = (P_i + K_{i \pmod m}) \pmod{26}$$
- **Decryption Formula:**
  $$P_i = (C_i - K_{i \pmod m}) \pmod{26}$$

#### Security Weaknesses:
- Repeating keyword introduces periodic patterns.
- Vulnerable to **Kasiski Examination** (finding repeated ciphertext sequences to determine key length $m$) and **Friedman's Index of Coincidence (IoC)**.

---

## 💻 Source Code Walkthrough

### 1. Caesar Cipher (`caesarcipher.py`)
```python
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
```

### 2. Vigenère Cipher (`vigenrecipher.py`)
```python
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
```

---

## 🚀 Execution & Verification

### Step 1: Run Caesar Cipher
```bash
python caesarcipher.py
```
**Sample Input:**
- Plaintext: `HELLOWORLD`
- Shift: `3`
- Ciphertext: `KHOORZRUOG`

![Caesar Cipher Execution Output](images/caesar%20output.png)

---

### Step 2: Run Vigenère Cipher
```bash
python vigenrecipher.py
```
**Sample Input:**
- Plaintext: `ATTACKATDAWN`
- Key: `LEMON`
- Ciphertext: `LXFOPVEFRNHR`

![Vigenère Cipher Execution Output](images/vigenere%20output.png)

---

## 🔍 Key Observations & Results
1. **Reversibility:** Both implementations correctly restore original plaintext upon decryption, verified automatically by the boolean assertion check (`Verification: True`).
2. **Case and Symbol Handling:** Alphabetic characters are shifted modulo 26 while spaces and punctuation remain preserved.
3. **Cryptographic Lesson:** Modern cryptosystems require non-linear confusion (S-boxes) and diffusion (P-boxes) across large key spaces ($\ge 128$ bits, e.g., AES) rather than simple linear modular shifts.
