import numpy as np
import json
from prototype import AetharShieldPrototype

def generate_challenge_files():
    print("[2026-08-13 05:31:46 WIB] Generating AetharShield Cryptanalysis Challenge Vectors...")
    cipher = AetharShieldPrototype()
    pub_key, priv_key = cipher.generate_keys()
    
    # Pesan rahasia yang disembunyikan (bit = 1)
    secret_bit = 1
    u, v = cipher.encrypt_bit(pub_key, secret_bit)
    
    # Aplikasikan DPL Permutation dengan seed acak rahasia
    secret_seed = 777888999
    u_permuted = cipher.apply_dpl_permutation(u, seed=secret_seed)
    
    challenge_data = {
        "parameters": {"n": cipher.n, "q": cipher.q},
        "public_key_t_sample": pub_key[1][:10].tolist(),
        "ciphertext_u_permuted_sample": u_permuted[:10].tolist(),
        "ciphertext_v": int(v)
    }
    
    print("\n[CHALLENGE VECTORS GENERATED]")
    print(json.dumps(challenge_data, indent=2))
    
if __name__ == "__main__":
    generate_challenge_files()