# Experiment 6: Secure Shell (SSH) Protocol & Traffic Analysis

## 🎯 Aim & Objectives
To analyze the architecture, cryptographic handshake, and packet flow of the **Secure Shell (SSH-2.0)** protocol over TCP Port 22:
- Understand the multi-layered SSH architecture (Transport, User Authentication, Connection).
- Trace the SSH connection lifecycle from TCP connection to encrypted channel multiplexing.
- Analyze algorithm negotiation, Diffie-Hellman key exchange, and host key verification.
- Compare SSH security guarantees with unencrypted legacy remote-access protocols (Telnet, Rlogin).

---

## 📚 Theoretical Background

### 1. SSH Protocol Architecture (RFC 4251 - 4254)
The SSH protocol operates over three distinct, tightly coupled layers:
1. **SSH Transport Layer Protocol (RFC 4253):** Provides server authentication, confidentiality, and data integrity with forward secrecy. Handles version exchange, algorithm negotiation, Diffie-Hellman key exchange, and key re-exchange.
2. **SSH User Authentication Protocol (RFC 4252):** Authenticates the client to the server using mechanisms such as `publickey`, `password`, or `hostbased`.
3. **SSH Connection Protocol (RFC 4254):** Multiplexes multiple logical channels (interactive shells, port forwarding, SFTP/SCP file transfer, X11 forwarding) over the single encrypted transport pipe.

```
+-------------------------------------------------------------+
|             SSH Connection Protocol (RFC 4254)              |
|        (Interactive Shell, Port Forwarding, SFTP)          |
+-------------------------------------------------------------+
|          SSH User Authentication Protocol (RFC 4252)        |
|               (Public Key, Password, GSSAPI)                |
+-------------------------------------------------------------+
|             SSH Transport Layer Protocol (RFC 4253)         |
|      (Confidentiality, Integrity, Key Exchange, Re-key)     |
+-------------------------------------------------------------+
|                         TCP / IP                            |
+-------------------------------------------------------------+
```

### 2. Handshake & Cryptographic Progression

```
 Client (Port > 1024)                               Server (Port 22)
        |                                                  |
        | ------------- 1. TCP 3-Way Handshake ----------> |
        | <----------------------------------------------- |
        |                                                  |
        | <----------- 2. Identification String ---------- |
        | ------------ (e.g., SSH-2.0-OpenSSH_9.3) ------> |
        |                                                  |
        | <----------- 3. SSH_MSG_KEXINIT ---------------- |
        | ------------ 4. SSH_MSG_KEXINIT ---------------> |
        |       (List of supported ciphers, KEX, MACs)     |
        |                                                  |
        | ------------ 5. SSH_MSG_KEXDH_INIT ------------> |
        |       (Client ephemeral public key e = g^x mod p)|
        |                                                  |
        | <----------- 6. SSH_MSG_KEXDH_REPLY ------------ |
        |       (Server host key K_S, ephemeral f, sig)    |
        |                                                  |
        | ------------ 7. SSH_MSG_NEWKEYS ---------------> |
        | <----------- 8. SSH_MSG_NEWKEYS ---------------- |
        |    (Subsequent packets encrypted with keys)      |
        |                                                  |
        | <======== Encrypted Authentication & Shell ====> |
```

---

## 🛠️ Step-by-Step Procedure & Protocol Verification

### Step 1: SSH Key Generation & Public Key Authentication
Generate modern cryptographic SSH keys using **Ed25519** (Edwards-curve Digital Signature Algorithm) or **RSA 4096-bit**:
```bash
# Generate high-security Ed25519 keypair
ssh-keygen -t ed25519 -C "analyst@security-lab"

# Or generate standard 4096-bit RSA keypair
ssh-keygen -t rsa -b 4096 -C "analyst@security-lab"
```

Inspect generated key files:
- Private Key (`id_ed25519`): Stored securely with permissions `600`.
- Public Key (`id_ed25519.pub`): Appended to target's `~/.ssh/authorized_keys`.

---

### Step 2: Protocol Version Exchange & Verbose Handshake Trace
Initiate an SSH session in verbose mode (`-v` or `-vvv`) to observe the handshake trace directly from the client terminal:
```bash
ssh -vvv user@192.168.64.6
```
**Handshake Highlights Observed:**
1. `Local version string SSH-2.0-OpenSSH_...`
2. `Remote protocol version 2.0, remote software version OpenSSH_...`
3. `SSH2_MSG_KEXINIT sent / received`
4. `kex: algorithm: curve25519-sha256`
5. `Host key: ED25519 SHA256:...`
6. `SSH2_MSG_NEWKEYS sent / received`
7. `Authenticated to 192.168.64.6 using "publickey"`

---

### Step 3: Wireshark Network Traffic Analysis
Capture live SSH packets using Wireshark:
1. Set capture filter: `tcp port 22`
2. Set display filter: `ssh`

#### Packet Sequence in Wireshark:
- **Packet 1-3:** Standard TCP 3-way handshake (`SYN`, `SYN-ACK`, `ACK`).
- **Packet 4-5:** Protocol Version Strings (`SSH-2.0-...`) visible in cleartext ASCII.
- **Packet 6-7:** `SSH_MSG_KEXINIT` packets listing supported key exchange algorithms, host key formats, ciphers (`chacha20-poly1305@openssh.com`, `aes256-gcm@openssh.com`), and MACs (`hmac-sha2-512`).
- **Packet 8-9:** Ephemeral Key Exchange parameters exchanged.
- **Packet 10-11:** `SSH_MSG_NEWKEYS` signaling that subsequent frames switch to negotiated symmetric encryption.
- **Subsequent Packets:** Labeled as `Encrypted packet (len=...)` — all commands, outputs, and keystrokes are indecipherable to an eavesdropper.

---

### Step 4: Host Key Fingerprinting & MITM Defense
Verify server identity to prevent Man-in-the-Middle attacks:
```bash
# Scan and query remote host keys
ssh-keyscan -t ed25519 -p 22 192.168.64.6

# Verify fingerprint against known_hosts
ssh-keygen -l -f ~/.ssh/known_hosts
```
- If an adversary intercepts traffic or replaces the server, SSH halts the connection with:
  `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`

---

## ⚖️ Security Comparison: SSH vs. Telnet

| Parameter | Telnet (Port 23) | SSH (Port 22) |
|---|---|---|
| **Confidentiality** | ❌ None (All traffic transmitted in cleartext) | ✅ Strong symmetric encryption (AES, ChaCha20) |
| **Authentication** | ❌ Cleartext passwords easily intercepted | ✅ Public key (Ed25519, RSA), Certificate, Multi-factor |
| **Integrity** | ❌ Vulnerable to TCP packet injection & tampering | ✅ HMAC-SHA256 / AEAD authentication tags |
| **Forward Secrecy** | ❌ Not applicable | ✅ Ephemeral Diffie-Hellman / Curve25519 |
| **Channel Multiplexing** | ❌ Single session per connection | ✅ Multiple channels, dynamic port forwarding (SOCKS) |

---

## 🔍 Key Observations & Results
1. **Cleartext Boundary:** Only the initial protocol version string (`SSH-2.0-...`) and algorithm lists (`KEXINIT`) are visible in transit; zero user data or credentials leak over the wire.
2. **Strict Host Verification:** SSH's Trust On First Use (TOFU) model effectively neutralizes opportunistic MITM spoofing.
3. **Cryptographic Agility:** Modern SSH-2.0 dynamically negotiates optimal cipher suites while gracefully deprecating insecure legacy ciphers (e.g., DES, 3DES, RC4).
