import numpy as np

class AetharNTT:
    def __init__(self, n=1024, q=12289, psi=1479):
        self.n = n
        self.q = q
        self.psi = psi
        self.omega = (psi * psi) % q
        
        # Precompute Powers of Psi (Twiddle Factors)
        self.psi_powers = [pow(self.psi, i, self.q) for i in range(self.n)]
        self.psi_inv_powers = [pow(pow(self.psi, i, self.q), self.q - 2, self.q) for i in range(self.n)]
        self.n_inv = pow(self.n, self.q - 2, self.q)

    def _bit_reverse_sort(self, a):
        """ Bit-reversal permutation """
        num_bits = int(np.log2(self.n))
        result = np.zeros_like(a)
        for i in range(self.n):
            rev_i = int(f"{i:0{num_bits}b}"[::-1], 2)
            result[rev_i] = a[i]
        return result

    def forward_ntt(self, poly):
        """ Fast Number Theoretic Transform O(n log n) """
        a = self._bit_reverse_sort(poly)
        a = a.astype(np.int64)
        
        len_step = 2
        while len_step <= self.n:
            half_len = len_step // 2
            step = self.n // len_step
            for i in range(0, self.n, len_step):
                for j in range(half_len):
                    w = self.psi_powers[j * step]
                    u = a[i + j]
                    v = (a[i + j + half_len] * w) % self.q
                    a[i + j] = (u + v) % self.q
                    a[i + j + half_len] = (u - v + self.q) % self.q
            len_step *= 2
        return a

    def inverse_ntt(self, poly):
        """ Fast Inverse Number Theoretic Transform O(n log n) """
        a = self._bit_reverse_sort(poly)
        a = a.astype(np.int64)
        
        len_step = 2
        while len_step <= self.n:
            half_len = len_step // 2
            step = self.n // len_step
            for i in range(0, self.n, len_step):
                for j in range(half_len):
                    w = self.psi_inv_powers[j * step]
                    u = a[i + j]
                    v = (a[i + j + half_len] * w) % self.q
                    a[i + j] = (u + v) % self.q
                    a[i + j + half_len] = (u - v + self.q) % self.q
            len_step *= 2
            
        return (a * self.n_inv) % self.q

    def ntt_multiply(self, poly_a, poly_b):
        """ Pointwise Multiplication dalam domain NTT """
        ntt_a = self.forward_ntt(poly_a)
        ntt_b = self.forward_ntt(poly_b)
        
        # Pointwise multiplication O(n)
        ntt_result = (ntt_a * ntt_b) % self.q
        
        # Convert kembali ke domain waktu O(n log n)
        return self.inverse_ntt(ntt_result)

if __name__ == "__main__":
    print("[2026-08-13 15:20:04 WIB] Testing AetharShield NTT Acceleration Engine...")
    ntt_engine = AetharNTT(n=1024, q=12289)
    
    # Dummy Polinomial
    p1 = np.random.randint(0, 10, size=1024)
    p2 = np.random.randint(0, 10, size=1024)
    
    result = ntt_engine.ntt_multiply(p1, p2)
    print("NTT Polynomial Multiplication Successful!")
    print("Sample Output Vector [0..5]:", result[:5])