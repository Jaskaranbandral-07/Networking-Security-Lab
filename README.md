# 🔒 Networking & Network Security Lab

> A comprehensive, hands-on cybersecurity laboratory covering **classical substitution cryptography**, **cryptographic hashing & integrity verification**, **challenge-response authentication & replay defenses**, **Public Key Infrastructure (PKI) with X.509 certificates**, **TLS handshake packet analysis**, and **SSH protocol architecture**.

![Domain](https://img.shields.io/badge/Domain-Network%20Security-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20|%20Windows-blue?style=for-the-badge)
![Tools](https://img.shields.io/badge/Tools-Python%20|%20OpenSSL%20|%20Wireshark-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

---

## 📋 Overview

This repository documents **6 structured network security laboratory experiments** demonstrating fundamental and applied cryptographic principles, network protocol security, and packet-level traffic dissection. Each experiment includes complete implementations, step-by-step procedures, execution outputs, and detailed architectural walkthroughs.

### 🧰 Tools & Technologies
- **Python 3.x** (`hashlib`, `hmac`, `secrets`, `time`)
- **OpenSSL CLI** (Key generation, X.509 v3 certificates, PKI chain validation)
- **Wireshark** (Network packet sniffing, protocol dissectors, TLS & SSH capture filters)
- **Bash / Terminal** (CLI execution and protocol debugging)

---

## 🧪 Experiments

| # | Experiment | Primary Tools | Category |
|---|---|---|---|
| **1** | [Classical Substitution Ciphers (Caesar & Vigenère)](Experiment-1-Classical-Ciphers/) | Python 3 | 🔐 Classical Cryptography |
| **2** | [Cryptographic Hashing & Integrity Verification (SHA-256)](Experiment-2-Cryptographic-Hashing-SHA256/) | Python (`hashlib`) | 🛡️ Data Integrity |
| **3** | [Challenge-Response Authentication & Replay Attack Defense](Experiment-3-Authentication-Replay-Defense/) | Python (`hmac`, `secrets`) | 🔑 Authentication Protocols |
| **4** | [Public Key Infrastructure (PKI) & X.509 Certificates](Experiment-4-PKI-X509-Certificates/) | OpenSSL CLI, RSA | 📜 PKI & Certificates |
| **5** | [TLS Handshake Protocol Analysis using Wireshark](Experiment-5-TLS-Handshake-Analysis/) | Wireshark, HTTPS/TLS | 📡 Network Traffic Analysis |
| **6** | [Secure Shell (SSH) Protocol & Traffic Analysis](Experiment-6-SSH-Protocol-Analysis/) | OpenSSH, Wireshark | 🕵️ Secure Remote Access |

---

## 🔬 What You'll Learn

- **Classical Cryptography:** Implement monoalphabetic shift (Caesar) and polyalphabetic substitution (Vigenère) ciphers; analyze modular arithmetic and frequency cryptanalysis weaknesses.
- **Cryptographic Hashes:** Compute SHA-256 digests; understand one-way properties, collision resistance, and demonstrate the Avalanche Effect with tamper detection.
- **Authentication Protocols:** Design zero-knowledge challenge-response protocols using HMAC-SHA256; eliminate replay attacks using cryptographic nonces and synchronized timestamp windows.
- **Public Key Infrastructure:** Generate 2048-bit RSA private keys; issue self-signed X.509 v3 certificates with Subject Alternative Name (SAN), Key Usage, and Basic Constraints; verify certificate trust chains and public key fingerprints.
- **TLS Handshake Dissection:** Capture live HTTPS traffic in Wireshark; dissect Client Hello, Server Hello, cipher suite negotiation, Diffie-Hellman parameter exchange, and session establishment.
- **SSH Architecture:** Analyze SSH-2.0 protocol layers (Transport, User Authentication, Connection); trace key exchange (`KEXINIT`), host key verification, and encrypted channel multiplexing.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed:
  ```bash
  python --version
  ```
- **OpenSSL CLI** installed:
  ```bash
  openssl version
  ```
- **Wireshark** packet analyzer installed:
  ```bash
  wireshark --version
  ```

### Repository Setup

```bash
# Clone this repository
git clone https://github.com/Jaskaranbandral-07/Networking-Security-Lab.git

# Navigate into the project
cd Networking-Security-Lab
```

---

## 📂 Repository Structure

```
Networking-Security-Lab/
├── README.md                                             # Main lab documentation
├── LICENSE                                               # MIT License
├── .gitignore                                            # Git ignore definitions
├── qr-codes/                                             # High-res QR codes & printable sheet
│   ├── ALL-QR-CODES-PRINTABLE.pdf                        # A4 Print-ready PDF (Single page)
│   ├── ALL-QR-CODES-PRINTABLE.png                        # A4 Print-ready 300 DPI PNG
│   ├── qr-main-repo.png                                  # Main repository QR code
│   ├── qr-experiment-1.png                               # Exp 1 QR code
│   ├── qr-experiment-2.png                               # Exp 2 QR code
│   ├── qr-experiment-3.png                               # Exp 3 QR code
│   ├── qr-experiment-4.png                               # Exp 4 QR code
│   ├── qr-experiment-5.png                               # Exp 5 QR code
│   └── qr-experiment-6.png                               # Exp 6 QR code
│
├── Experiment-1-Classical-Ciphers/                       # Caesar & Vigenère ciphers
│   ├── README.md
│   ├── caesarcipher.py
│   ├── vigenrecipher.py
│   └── images/
│
├── Experiment-2-Cryptographic-Hashing-SHA256/            # SHA-256 hashing & integrity check
│   ├── README.md
│   ├── 01_sha256_hash.py
│   ├── 02_hash_verification.py
│   ├── 03_integrity_check.py
│   ├── sample.txt
│   └── images/
│
├── Experiment-3-Authentication-Replay-Defense/           # HMAC challenge-response & nonces
│   ├── README.md
│   ├── challenge_response.py
│   ├── replay_attack.py
│   ├── timestamp_check.py
│   └── images/
│
├── Experiment-4-PKI-X509-Certificates/                   # OpenSSL X.509 PKI certificates
│   ├── README.md
│   ├── x509_certificate.sh
│   ├── x509_certificate.py
│   ├── certificate.crt
│   └── images/
│
├── Experiment-5-TLS-Handshake-Analysis/                  # Wireshark TLS capture & analysis
│   ├── README.md
│   └── images/
│
└── Experiment-6-SSH-Protocol-Analysis/                   # OpenSSH protocol & packet dissection
    ├── README.md
    └── images/
```

---

## 📱 Quick Access (QR Codes)

All experiments include styled QR codes for rapid mobile access and submission. A single-page, high-resolution A4 print sheet is available in the [`qr-codes/`](qr-codes/) directory:
- [📄 Download Printable A4 Sheet (PDF)](qr-codes/ALL-QR-CODES-PRINTABLE.pdf)
- [🖼️ View Printable A4 Sheet (PNG)](qr-codes/ALL-QR-CODES-PRINTABLE.png)

---

## ⚠️ Disclaimer

> **Educational Use Only:** All scripts, configurations, and packet capture walkthroughs provided in this repository are strictly for academic and defensive educational purposes. Unauthorized interception, decryption, or tampering of network communications on systems without explicit permission is illegal and unethical.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) - feel free to use and adapt it for learning.

---

<p align="center">
  Made with 🔐 by <a href="https://github.com/Jaskaranbandral-07">Jaskaran Bandral</a>
</p>
