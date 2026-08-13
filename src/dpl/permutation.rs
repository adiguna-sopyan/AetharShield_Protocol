pub struct DynamicPermutation;

impl DynamicPermutation {
    // PRNG XORShift64 sederhana berbasis seed untuk Fisher-Yates Shuffle
    fn next_u64(state: &mut u64) -> u64 {
        let mut x = *state;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        *state = x;
        x
    }

    // Cryptographically Robust Fisher-Yates Permutation
    pub fn permute(data: &mut Vec<i64>, seed: u64) {
        let len = data.len();
        let mut state = if seed == 0 { 0x9E3779B97F4A7C15 } else { seed };

        for i in (1..len).rev() {
            let rand_val = Self::next_u64(&mut state);
            let j = (rand_val as usize) % (i + 1);
            data.swap(i, j);
        }
    }

    pub fn unpermute(data: &mut Vec<i64>, seed: u64) {
        let len = data.len();
        let mut state = if seed == 0 { 0x9E3779B97F4A7C15 } else { seed };

        // Precompute sequence of swap pairs
        let mut swaps = Vec::with_capacity(len);
        for i in (1..len).rev() {
            let rand_val = Self::next_u64(&mut state);
            let j = (rand_val as usize) % (i + 1);
            swaps.push((i, j));
        }

        // Reverse swaps to unpermute
        for (i, j) in swaps.into_iter().rev() {
            data.swap(i, j);
        }
    }
}