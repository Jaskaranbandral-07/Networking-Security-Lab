import hashlib

file = open("sample.txt", "rb")
data = file.read()
file.close()

original_hash = hashlib.sha256(data).hexdigest()

print("Original Hash:")
print(original_hash)

# Modify one character
file = open("sample.txt", "w")
file.write("network Security is important.")
file.close()

file = open("sample.txt", "rb")
data = file.read()
file.close()

new_hash = hashlib.sha256(data).hexdigest()

print("\nNew Hash:")
print(new_hash)

if original_hash == new_hash:
    print("Verification: MATCH")
else:
    print("Verification: MISMATCH")
