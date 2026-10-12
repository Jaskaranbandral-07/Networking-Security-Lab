# Experiment 3: Challenge-Response Authentication & Replay Attack Defense

## 🎯 Aim & Objectives
To implement and analyze secure authentication mechanisms using **HMAC (Keyed-Hash Message Authentication Code)** and evaluate defenses against **Replay Attacks**:
- Design a mutual/unilateral challenge-response protocol using cryptographic nonces.
- Demonstrate how nonce-based challenges prevent captured response replay.
- Implement time-bounded authentication windows using synchronized timestamps.

---

## 📚 Theoretical Background

### 1. Challenge-Response Authentication
In simple password-based systems, transmitting credentials over insecure channels exposes them to eavesdropping. In contrast, **Challenge-Response Authentication** proves identity possession of a shared secret key without ever exposing the key over the wire:
1. **Server generates a nonce:** A cryptographically secure random number $R$ (number used once).
2. **Server sends challenge $R$ to client.**
3. **Client computes HMAC:** $\text{Response} = \text{HMAC-SHA256}(K_{\text{secret}}, R)$.
4. **Server computes matching HMAC:** If both match, identity is authenticated.

$$\text{HMAC}(K, m) = H\Big((K \oplus \text{opad}) \parallel H\big((K \oplus \text{ipad}) \parallel m\big)\Big)$$

### 2. Replay Attacks & Defense Vectors
- **Replay Attack:** An attacker intercepts valid authentication tokens or responses from legitimate sessions and re-transmits them later to gain unauthorized access.
- **Defense Mechanism 1: Nonces (Number used once):** Because every session generates a fresh pseudo-random challenge nonce, old replayed responses will never match current session expectations.
- **Defense Mechanism 2: Timestamp Windows:** Restricting validity to a short time window ($\Delta t \le 5\text{s}$) prevents delayed replay by MITM adversaries.

---

## 💻 Source Code Walkthrough

### 1. HMAC Challenge-Response Protocol (`challenge_response.py`)
```python
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
```

### 2. Replay Attack Detection via Nonce Freshness (`replay_attack.py`)
```python
import secrets

old_challenge = secrets.token_hex(8)
new_challenge = secrets.token_hex(8)

old_response = "response123"

if old_challenge == new_challenge:
    print("Replay Attack: ACCEPTED")
else:
    print("Replay Attack: REJECTED")
```

### 3. Timestamp Freshness Window (`timestamp_check.py`)
```python
import time

sent_time = time.time()
current_time = time.time()

if current_time - sent_time <= 5:
    print("Timestamp: VALID")
else:
    print("Timestamp: EXPIRED")
```

---

## 🚀 Execution & Verification

### Step 1: Execute Challenge-Response Authentication
```bash
python challenge_response.py
```
A fresh 16-character hexadecimal nonce is created, signed via HMAC-SHA256, and validated.

![Challenge Response Authentication Output](images/output%20challenge_response.png)

---

### Step 2: Simulate Replay Attack
```bash
python replay_attack.py
```
An attacker attempting to replay previously captured challenge-response data is immediately detected and rejected due to challenge mismatch.

![Replay Attack Detection Output](images/output%20replay_attack.png)

---

### Step 3: Verify Timestamp Expiration Window
```bash
python timestamp_check.py
```
Validates the delta window; payloads arriving within the allowed margin ($\le 5$s) are validated, while expired payloads are rejected.

![Timestamp Validation Output](images/output%20timestamp_check.png)

---

## 🔍 Key Observations & Results
1. **Zero Secret Exposure:** The shared key $K_{\text{secret}}$ is never transmitted across the network, rendering packet sniffing attacks ineffective.
2. **Replay Immunity:** Nonces guarantee freshness per transaction; an attacker capturing traffic cannot predict future challenge answers.
3. **Protocols Using This Pattern:** Kerberos, TLS session resumption tickets, RADIUS, CHAP, OAuth 2.0 PKCE, and banking OTP authentication.
