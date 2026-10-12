import hashlib

file = open("sample.txt", "rb")
data = file.read()
file.close()

hash_value = hashlib.sha256(data).hexdigest()

print("SHA-256 Hash:")
print(hash_value)
print("Hash Length:", len(hash_value))
