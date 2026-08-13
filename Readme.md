# AetherShield Protocol

> **A Next-Gen Post-Quantum Cryptographic Primitive Layer with Dynamic Noise-Injected Lattice (HD-NIL) & Ephemeral Bit Permutation.**

![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Security Level](https://img.shields.io/badge/security-NIST--Level--5-orange)

## Overview

**AetherShield** is an experimental, post-quantum cryptographic architecture designed to provide long-term confidentiality against both classical computers and Quantum Annealers/CRQCs (Cryptographically Relevant Quantum Computers). 

By combining **High-Dimensional Learning With Errors (LWE)** with a non-linear **Dynamic Permutation Layer (DPL)**, AetherShield mitigates standard lattice-reduction vector attacks while maintaining a low computational footprint for constant-time hardware execution.

---

## Key Features

- **HD-NIL Core:** Powered by $n=1024$ dimension vector lattice over $\mathbb{Z}_q$ ($q=12289$) with Gaussian error distribution $\chi(\sigma)$.
- **Dynamic Permutation Layer (DPL):** Ephemeral non-linear bit permutation applied post-encryption to break linear lattice analysis.
- **Side-Channel Resistant:** Core operations implemented in strict constant-time Rust logic to block timing attacks.
- **Zero-External-Crypto Dependency:** Native implementation of Number Theoretic Transform (NTT) polynomial multiplication for auditability.

---

## Mathematical Specification

AetherShield operates on the LWE hardness assumption over polynomial rings:

$$t = (A \cdot s + e) \pmod q$$

Post-LWE encryption vectors $(u, v)$ undergo an ephemeral permutation transformation:

$$\text{Ciphertext}_{\text{final}} = \mathcal{P}_{\text{seed}}(u, v)$$

For a complete mathematical proof and parameter breakdown, see [docs/WHITEPAPER.md](docs/WHITEPAPER.md).

---

## Quickstart (Python Prototype)

```bash
# Clone the repositorya
git clone [https://github.com/adiguna-sopyan/AetherShield_protocol.git](https://github.com/adiguna-sopyan/AetherShield_protocol.git)
cd aether-shield/python-bindings

# Run test vectorsqq
python3 -m unittest discover tests
```

### Basic Usage Example

```python
from aethershield import AetherShield

# Initialize AetherShield Engine (n=1024, q=12289)
cipher = AetherShield()

# Generate Keypair
pub_key, priv_key = cipher.generate_keypair()

# Encrypt Message Bit
message_bit = 1
ciphertext = cipher.encrypt(pub_key, message_bit)

# Decrypt Message Bit
decrypted_bit = cipher.decrypt(priv_key, ciphertext)

assert message_bit == decrypted_bit
print("AetherShield Encryption & Decryption Successful.")
```

---

## Security Disclaimer & Cryptanalysis Challenge

AetherShield is currently in **Phase 2 (Open Specification & Prototyping)**. It is released for peer-review, cryptanalysis, and research purposes. **Do not deploy in production environments prior to formal academic review.**

We actively invite researchers to break the implementation. Test vectors and target challenges are located in `/docs/CHALLENGE.md`.

---

## License

Dual-licensed under either of:
- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE) or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE) or http://opensource.org/licenses/MIT)
