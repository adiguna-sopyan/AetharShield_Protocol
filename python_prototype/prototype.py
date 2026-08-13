import numpy as np
import time

class AetharShieldPrototype:
    def __init__(self, n=1024, q=12289):
        self.n = n  # Dimensi Vektor Lattice
        self.q = q  # Modulus

    def generate_keys(self):
        # Secret Key (s): Vektor biner rahasia
        s = np.random.randint(0, 2, size=self.n)
        # Matriks Publik (A)
        A = np.random.randint(0, self.q, size=(self.n, self.n))
        # Injeksi Noise / Error (e)
        e = np.random.randint(-1, 2, size=self.n)
        # Kunci Publik: t = (A*s + e) mod q
        t = (np.dot(A, s) + e) % self.q
        return (A, t), s

    def encrypt_bit(self, public_key, bit):
        A, t = public_key
        r = np.random.randint(0, 2, size=self.n)
        e1 = np.random.randint(-1, 2, size=self.n)
        e2 = np.random.randint(-1, 2)

        # Ciphertext Vectors (u, v)
        u = (np.dot(A.T, r) + e1) % self.q
        v = (np.dot(t, r) + e2 + bit * (self.q // 2)) % self.q
        return u, v

    def apply_dpl_permutation(self, u, seed=42):
        # Secure Fisher-Yates Permutation
        permuted_u = u.copy()
        n = len(permuted_u)
        state = seed & 0xFFFFFFFF  # Masking 32-bit agar aman di NumPy
        
        for i in range(n - 1, 0, -1):
            state = (state * 1103515245 + 12345) & 0x7FFFFFFF  # LCG Generator
            j = state % (i + 1)
            permuted_u[i], permuted_u[j] = permuted_u[j], permuted_u[i]
            
        return permuted_u

    def restore_dpl_permutation(self, permuted_u, seed=42):
        # Restore Fisher-Yates Permutation
        unshuffled_u = permuted_u.copy()
        n = len(unshuffled_u)
        state = seed & 0xFFFFFFFF
        
        swaps = []
        for i in range(n - 1, 0, -1):
            state = (state * 1103515245 + 12345) & 0x7FFFFFFF
            j = state % (i + 1)
            swaps.append((i, j))
            
        for i, j in reversed(swaps):
            unshuffled_u[i], unshuffled_u[j] = unshuffled_u[j], unshuffled_u[i]
            
        return unshuffled_u

    def decrypt_bit(self, secret_key, u, v):
        # Dekripsi
        noisy_signal = (v - np.dot(secret_key, u)) % self.q
        target = self.q // 2
        diff = min((noisy_signal - target) % self.q, (target - noisy_signal) % self.q)
        return 1 if diff < (self.q // 4) else 0

if __name__ == "__main__":
    print("[2026-08-12 22:31:05 WIB] Initializing Full AetharShield Protocol Test Cycle...\n")
    
    cipher = AetharShieldPrototype()
    
    # 1. Key Generation
    t_start = time.time()
    pub_key, priv_key = cipher.generate_keys()
    print(f"[1] Keypair Generated in {time.time() - t_start:.4f}s")
    
    # 2. Encrypt Message Bit (m = 1)
    original_bit = 1
    u, v = cipher.encrypt_bit(pub_key, original_bit)
    print(f"[2] Message Bit '{original_bit}' Encrypted to Ciphertext (u, v)")
    
    # 3. Apply DPL (Dynamic Permutation Layer)
    seed_ephemeral = 998244353
    u_permuted = cipher.apply_dpl_permutation(u, seed=seed_ephemeral)
    print(f"[3] DPL Permutation Applied to Ciphertext u using Seed: {seed_ephemeral}")
    
    # 4. Restore DPL & Decrypt
    u_restored = cipher.restore_dpl_permutation(u_permuted, seed=seed_ephemeral)
    decrypted_bit = cipher.decrypt_bit(priv_key, u_restored, v)
    print(f"[4] Decrypted Message Bit: {decrypted_bit}")
    
    # 5. Validation
    status = "SUCCESS" if original_bit == decrypted_bit else "FAILED"
    print(f"\n==========================================")
    print(f" AetharShield Test Result: {status}")
    print(f"==========================================")