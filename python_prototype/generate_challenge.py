import numpy as np
import json
import os
from prototype import AetharShieldPrototype

def generate_full_challenge():
    print("[2026-08-13 21:52:14 WIB] Generating Full Level-2 Challenge Matrices (A, t)...")
    cipher = AetharShieldPrototype()
    pub_key, priv_key = cipher.generate_keys()
    
    A, t = pub_key
    secret_bit = 1
    u, v = cipher.encrypt_bit(pub_key, secret_bit)
    
    # Secure Seed DPL
    secret_seed = 0xDEADBEEF
    u_permuted = cipher.apply_dpl_permutation(u, seed=secret_seed)
    
    challenge_payload = {
        "parameters": {"n": cipher.n, "q": cipher.q},
        "public_key_A": A.tolist(),
        "public_key_t": t.tolist(),
        "ciphertext_u_permuted": u_permuted.tolist(),
        "ciphertext_v": int(v),
        "note": "Full Level-2 Challenge: Recover the binary secret vector s (length 1024) or the secret message bit."
    }
    
    output_path = os.path.join("docs", "challenge_data.json")
    with open(output_path, "w") as f:
        json.dump(challenge_payload, f)
        
    print(f"[SUCCESS] Full Challenge Dataset published to: {output_path}")

if __name__ == "__main__":
    generate_full_challenge()