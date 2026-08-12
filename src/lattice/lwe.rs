use crate::{DIMENSION_N, MODULUS_Q};
use rand::Rng;

pub struct LweEngine {
    pub n: usize,
    pub q: i64,
}

impl LweEngine {
    pub new() -> Self {
        Self {
            n: DIMENSION_N,
            q: MODULUS_Q,
        }
    }

    pub fn generate_keypair(&self) -> (Vec<Vec<i64>>, Vec<i64>, Vec<i64>) {
        let mut rng = rand::thread_rng();
        
        // Secret Key (s) - Vektor biner
        let secret_key: Vec<i64> = (0..self.n).map(|_| rng.gen_range(0..=1)).collect();
        
        // Matriks Publik (A)
        let mut matrix_a = vec![vec![0i64; self.n]; self.n];
        for i in 0..self.n {
            for j in 0..self.n {
                matrix_a[i][j] = rng.gen_range(0..self.q);
            }
        }
        
        // Injeksi Noise / Error (e) - Gaussian noise kecil
        let noise: Vec<i64> = (0..self.n).map(|_| rng.gen_range(-1..=1)).collect();
        
        // Kunci Publik: t = (A * s + e) mod q
        let mut public_key = vec![0i64; self.n];
        for i in 0..self.n {
            let mut sum = 0i64;
            for j in 0..self.n {
                sum = (sum + matrix_a[i][j] * secret_key[j]) % self.q;
            }
            public_key[i] = (sum + noise[i] + self.q) % self.q;
        }

        (matrix_a, public_key, secret_key)
    }
}