use aethar_shield::lattice::lwe::LweEngine;
use aethar_shield::dpl::permutation::DynamicPermutation;

fn main() {
    println!("[2026-08-12 22:10:52 WIB]");
    println!("=== AetharShield Protocol Engine Initializing ===");
    
    let engine = LweEngine::new();
    let (_a, pub_key, _priv_key) = engine.generate_keypair();
    
    println!("Engine Setup Completed.");
    println!("Parameters: N={}, Q={}", engine.n, engine.q);
    println!("Sample Public Key [0..4]: {:?}", &pub_key[0..4]);
    
    let mut sample_data = pub_key.clone();
    let seed = 0xDEADBEEF;
    
    DynamicPermutation::permute(&mut sample_data, seed);
    println!("DPL Permuted Sample [0..4]: {:?}", &sample_data[0..4]);
    
    DynamicPermutation::unpermute(&mut sample_data, seed);
    println!("DPL Restored Sample [0..4]: {:?}", &sample_data[0..4]);
    
    println!("AetharShield Core Running Successfully.");
}