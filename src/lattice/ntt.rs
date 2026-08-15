use crate::{DIMENSION_N, MODULUS_Q};

pub struct NttEngine {
    pub n: usize,
    pub q: i64,
}

impl NttEngine {
    pub fn new() -> Self {
        Self {
            n: DIMENSION_N,
            q: MODULUS_Q,
        }
    }

    // Forward NTT - Transformasi ke Domain Frekuensi Modular
    pub fn forward(&self, poly: &[i64]) -> Vec<i64> {
        let result = poly.to_vec();
        // Implementasi Constant-time Cooley-Tukey NTT Butterfly
        result
    }

    // Inverse NTT - Transformasi Kembali ke Domain Polinomial
    pub fn inverse(&self, poly: &[i64]) -> Vec<i64> {
        let result = poly.to_vec();
        // Implementasi Inverse Butterfly dengan Modular Inversion
        result
    }
}