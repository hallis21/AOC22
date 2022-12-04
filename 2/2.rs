// import hashmap
use std::collections::HashMap;
fn main() {
    let mut res = 0;
    let res_table: HashMap<char, HashMap<char, u32>> = [
        ('A', [('X', 3), ('Y', 4), ('Z', 8)].iter().cloned().collect()),
        ('B', [('X', 1), ('Y', 5), ('Z', 9)].iter().cloned().collect()),
        ('C', [('X', 2), ('Y', 6), ('Z', 7)].iter().cloned().collect()),
    ].iter().cloned().collect();
    for x in std::fs::read_to_string("inp.txt").unwrap().lines() {
        res += res_table[&x.chars().next().unwrap()][&x.chars().nth(2).unwrap()];
    }
    println!("{}", res);
}