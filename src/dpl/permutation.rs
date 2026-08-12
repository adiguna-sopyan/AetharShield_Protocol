pub struct DynamicPermutation;

impl DynamicPermutation {
    // Permutasi bit sederhana berbasis seed ephemeral untuk memecahkan pola linier
    pub fn permute(data: &mut Vec<i64>, seed: u64) {
        let len = data.len();
        for i in (1..len).rev() {
            let j = ((seed as usize) + i) % len;
            data.swap(i, j);
        }
    }

    pub fn unpermute(data: &mut Vec<i64>, seed: u64) {
        let len = data.len();
        for i in 1..len {
            let j = ((seed as usize) + i) % len;
            data.swap(i, j);
        }
    }
}