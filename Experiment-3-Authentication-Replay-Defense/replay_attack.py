import secrets

old_challenge = secrets.token_hex(8)
new_challenge = secrets.token_hex(8)

old_response = "response123"

if old_challenge == new_challenge:
    print("Replay Attack: ACCEPTED")
else:
    print("Replay Attack: REJECTED")
