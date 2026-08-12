# AetharShield Cryptanalysis Challenge

Welcome to the **AetharShield Protocol Cryptanalysis Challenge**. 

This challenge is designed for security researchers, cryptographers, and mathematicians to test the security boundaries of the AetharShield architecture against classical lattice-reduction algorithms (e.g., LLL, BKZ) and PRNG seed recovery attacks.

---

## Challenge Level 1: DPL Permutation Recovery (Medium)
- **Objective:** Recover the hidden binary message $m \in \{0, 1\}$.
- **Parameters:** $N = 1024$, $Q = 12289$
- **Given:** Public Key $(A, t)$, Ciphertext $(u_{\text{permuted}}, v)$.
- **Target Condition:** The ciphertext $u$ has been shuffled using an unknown 32-bit ephemeral DPL seed. Decrypt $m$ without knowing the seed or private key $s$.

---

## Challenge Level 2: LWE Secret Vector Recovery (Hard)
- **Objective:** Recover the binary Secret Vector $s \in \{0, 1\}^{1024}$.
- **Parameters:** Matrix $A \in \mathbb{Z}_{12289}^{1024 \times 1024}$, Vector $t \in \mathbb{Z}_{12289}^{1024}$.
- **Mathematical Relation:** $t = (A \cdot s + e) \pmod q$, where $e_i \in \{-1, 0, 1\}$.
- **Target Condition:** Find $s$ given only $A$ and $t$.

---

## Submission & Disclosure
If you discover a mathematical weakness, key recovery vector, or successful side-channel leak:
1. Open a **GitHub Issue** titled `[Cryptanalysis] Solution Challenge Level X`.
2. Provide your execution script, time complexity proof, and recovered secret.
3. Successful cryptanalysis will be credited in the `WHITEPAPER.md` acknowledgement section.