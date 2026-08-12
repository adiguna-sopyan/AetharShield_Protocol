import numpy as np

class AetharShieldPrototype:
    def __init__(self, n=1024, q=12289):
        self.n = n
        self.q = q

    def generate_keys(self):
        s = np.random.randint(0, 2, size=self.n)
        A = np.random.randint(0, self.q, size=(self.n, self.n))
        e = np.random.randint(-1, 2, size=self.n)
        t = (np.dot(A, s) + e) % self.q
        return (A, t), s

if __name__ == "__main__":
    print("[2026-08-12 22:10:52 WIB] Running AetharShield Python Prototype...")
    cipher = AetharShieldPrototype()
    pub, priv = cipher.generate_keys()
    print("Keys generated successfully. Public key shape:", pub[1].shape)