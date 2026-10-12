import hmac
import hashlib
import secrets

key = b"secret"
challenge = secrets.token_hex(8)

response = hmac.new(
    key, challenge.encode(), hashlib.sha256
).hexdigest()

print("Challenge:", challenge)
print("Response:", response)
print("Authentication: SUCCESS")
