import hashlib

file = open("sample.txt", "rb")
data = file.read()
file.close()

current_hash = hashlib.sha256(data).hexdigest()

trusted_hash = input("Enter trusted SHA-256 hash: ")

print("Trusted Hash :", trusted_hash)
print("Current Hash :", current_hash)

if trusted_hash == current_hash:
    print("Verification: MATCH")
else:
    print("Verification: MISMATCH")
