use std::io::*;
fn main() {
    let mut c_v: Vec<u8> = Vec::new();
    let v: Vec<u8> = vec![97, 100, 104, 109, 112, 96, 98, 97, 100, 79, 124, 115, 76, 125, 74, 117, 118, 118, 70, 109, 105, 117, 105, 123, 64, 73, 79, 125, 81, 81, 86, 82, 90];

    let mut input = String::new();
    stdin().read_line(&mut input).expect("Did not enter a correct string");
    let input = input.trim().to_string();

    for (i, c) in input.as_bytes().iter().enumerate() {
        c_v.push(c ^ (i as u8 + 7));
    }

    if vec_compare(&v, &c_v) == true {
        println!("nice job");
    } else {
        println!("you fail");
    }
}
fn eq_with_nan_eq(a: u8, b: u8) -> bool {
    a == b
}

fn vec_compare(va: &[u8], vb: &[u8]) -> bool {
    (va.len() == vb.len()) &&  // zip stops at the shortest
     va.iter()
       .zip(vb)
       .all(|(a,b)| eq_with_nan_eq(*a,*b))
}
