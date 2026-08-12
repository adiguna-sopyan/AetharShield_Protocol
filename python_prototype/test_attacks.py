import numpy as np
from prototype import AetharShieldPrototype

def run_cryptanalysis_tests():
    print("[2026-08-12 22:33:15 WIB] Running AetharShield Cryptanalysis Tests...\n")
    cipher = AetharShieldPrototype()
    pub_key, priv_key = cipher.generate_keys()
    
    original_bit = 1
    u, v = cipher.encrypt_bit(pub_key, original_bit)
    
    correct_seed = 998244353
    wrong_seed = 123456789
    
    u_permuted = cipher.apply_dpl_permutation(u, seed=correct_seed)
    
    # Skenario A: Peretas mencoba dekripsi dengan SEED DPL SALAH
    u_bad_unshuffle = cipher.restore_dpl_permutation(u_permuted, seed=wrong_seed)
    decrypted_bad_seed = cipher.decrypt_bit(priv_key, u_bad_unshuffle, v)
    
    # Skenario B: Peretas mencoba dekripsi dengan KUNCI RAHASIA SALAH
    wrong_priv_key = np.random.randint(0, 2, size=cipher.n)
    u_correct_unshuffle = cipher.restore_dpl_permutation(u_permuted, seed=correct_seed)
    decrypted_bad_key = cipher.decrypt_bit(wrong_priv_key, u_correct_unshuffle, v)
    
    print(f"Pesan Asli                     : {original_bit}")
    print(f"Serangan 1 (DPL Seed Salah)   : Bit Hasil Dekripsi = {decrypted_bad_seed} -> {'GAGAL / AMAN' if decrypted_bad_seed != original_bit else 'TEREKSPOS'}")
    print(f"Serangan 2 (Kunci Rahasia Salah): Bit Hasil Dekripsi = {decrypted_bad_key} -> {'GAGAL / AMAN' if decrypted_bad_key != original_bit else 'TEREKSPOS'}")

if __name__ == "__main__":
    run_cryptanalysis_tests()